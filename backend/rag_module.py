import os
import json
import torch
import faiss
import numpy as np
from sentence_transformers import SentenceTransformer, util
from langchain_community.embeddings import HuggingFaceEmbeddings
import together
from backend.models.inlegalbert_model import QAModel, LegalEmbeddingModel
from dotenv import load_dotenv

# -------------------------------------------------------------------------
# 🔹 Load environment variables (Together API)
# -------------------------------------------------------------------------
load_dotenv()
TOGETHER_API_KEY = os.getenv("TOGETHER_API_KEY")
together.api_key = TOGETHER_API_KEY

device = "cuda" if torch.cuda.is_available() else "cpu"

# -------------------------------------------------------------------------
# 🔹 Load Models and Data Once
# -------------------------------------------------------------------------
QUESTION_EMB_PATH = "backend/data/question_embeddings.pt"
FAISS_INDEX_PATH = "backend/data/faiss_index/legal_faiss.index"
CHUNKS_PATH = "backend/data/legal_chunks.npy"
LEGAL_DB_PATH = "backend/data/legal_data.json"

print("🔹 Loading models and data...")

model = QAModel()                      # SentenceTransformer for QA
embedding_model = LegalEmbeddingModel()  # InLegalBERT for law chunks

# Load question embeddings and questions
data = torch.load(QUESTION_EMB_PATH, weights_only=False)
question_embeddings = data["embeddings"].float()
questions = data["questions"]

# Load FAISS index and legal chunks
faiss_index = faiss.read_index(FAISS_INDEX_PATH)
legal_chunks = np.load(CHUNKS_PATH, allow_pickle=True)

# Load QA database
if os.path.exists(LEGAL_DB_PATH):
    with open(LEGAL_DB_PATH, "r", encoding="utf-8") as f:
        qa_data = json.load(f)
        answers = {item["question"]: item["answer"] for item in qa_data}
else:
    answers = {}

print("✅ RAG Module initialized successfully.")

# -------------------------------------------------------------------------
# 🔹 Helper Functions
# -------------------------------------------------------------------------
def find_closest_match(user_question: str):
    """Find closest matching QA question using SentenceTransformer."""
    user_embedding = model.encode(user_question)  # tensor on GPU if available

    # move everything to the same device
    if isinstance(user_embedding, np.ndarray):
        user_embedding = torch.tensor(user_embedding)
    user_embedding = user_embedding.to(device)

    q_emb = question_embeddings.to(device)

    similarities = util.pytorch_cos_sim(user_embedding, q_emb)
    best_match_idx = similarities.argmax().item()

    best_match_question = questions[best_match_idx]
    similarity_score = similarities[0][best_match_idx].item()
    return best_match_question, similarity_score


def search_legal_docs(query: str, top_k: int = 5):
    """Search top-k relevant law chunks using FAISS + cosine re-ranking."""
    query_embedding = np.array(embedding_model.embed(query)).astype("float32").reshape(1, -1)

    if query_embedding.shape[1] != faiss_index.d:
        raise ValueError(
            f"❌ Dimension mismatch: Query dim = {query_embedding.shape[1]}, "
            f"FAISS index dim = {faiss_index.d}"
        )

    distances, indices = faiss_index.search(query_embedding, top_k)
    retrieved_chunks = [legal_chunks[idx] for idx in indices[0]]

    # Re-rank with cosine similarity (keep both tensors on same device)
    query_vector = torch.tensor(query_embedding, dtype=torch.float32, device=device)
    chunk_vectors = torch.tensor(
        np.array([embedding_model.embed([chunk])[0] for chunk in retrieved_chunks]),
        dtype=torch.float32,
        device=device
    )

    scores = util.pytorch_cos_sim(query_vector, chunk_vectors)[0]
    ranked_chunks = sorted(zip(retrieved_chunks, scores), key=lambda x: x[1], reverse=True)
    best_chunk, _ = ranked_chunks[0]

    # --- Generate answer ---
    model_name = "mistralai/Mistral-7B-Instruct-v0.2"
    prompt = f"""
    As a legal chatbot specializing in Indian Penal Code, respond with accurate and structured legal information.

    Guidelines:
    - Respond in 5 bullet points covering distinct legal aspects.
    - First mention which law or section the context falls under.
    - Each point should reflect real legal provisions and clarify applicability.
    - Avoid unnecessary assumptions; stay factual.

    CONTEXT: {best_chunk}

    QUESTION: {query}
    ANSWER:
    """

    try:
        response = together.Complete.create(
            model=model_name,
            prompt=prompt,
            max_tokens=300,
            temperature=1
        )
        if "choices" in response and response["choices"]:
            return response["choices"][0]["text"].strip()
        else:
            return "⚠️ No response received from Together AI."
    except Exception as e:
        return f"❌ Error generating answer: {e}"


def get_answer(user_question: str):
    """Main function to handle QA retrieval pipeline."""
    best_match_question, similarity_score = find_closest_match(user_question)

    if similarity_score >= 0.7:
        # High similarity — use stored Q&A
        answer_text = answers.get(best_match_question, "Answer not found in database.")
        return {
            "type": "Q&A Match",
            "question": best_match_question,
            "similarity": round(similarity_score, 2),
            "answer": answer_text
        }

    elif 0.3 < similarity_score < 0.7:
        # Moderate similarity — use document retrieval
        generated_answer = search_legal_docs(user_question)
        return {
            "type": "RAG Generation",
            "similarity": round(similarity_score, 2),
            "generated_answer": generated_answer
        }

    else:
        # Low similarity — no reliable match
        return {
            "type": "No Match",
            "similarity": round(similarity_score, 2),
            "message": "Sorry, no relevant legal information found at the moment."
        }
