
import os, json, numpy as np, faiss
from sentence_transformers import SentenceTransformer
from sentence_transformers.cross_encoder import CrossEncoder
from dotenv import load_dotenv

load_dotenv()
DATA_PATH = "backend/data/summarized_legal_data.json"
INDEX_PATH = "backend/data/faiss_index/advice_index.index"
MODEL_PATH = "backend/models/fine_tuned_inlegalbert"

print("🔹 Loading advice data and models...")

with open(DATA_PATH, "r", encoding="utf-8") as f:
    data = json.load(f)

index = faiss.read_index(INDEX_PATH)


model = SentenceTransformer(MODEL_PATH)


reranker = CrossEncoder("cross-encoder/ms-marco-MiniLM-L-6-v2")

print(f"✅ Loaded {len(data)} advice entries and FAISS index.")


def get_legal_advice(user_question: str, top_k: int = 10, threshold: float = 0.2):
    """
    Retrieves the most relevant legal advice entries from the summarized dataset.
    Uses FAISS for dense retrieval and a CrossEncoder for reranking.
    """
    
    query_embedding = model.encode(user_question, convert_to_numpy=True)
    query_embedding = np.array(query_embedding).reshape(1, -1).astype("float32")
    faiss.normalize_L2(query_embedding)

    
    D, I = index.search(query_embedding, top_k)
    similarity_scores = D[0]

    candidates = []
    for idx, i in enumerate(I[0]):
        if i < len(data):
            item = data[i].copy()
            item["similarity"] = float(similarity_scores[idx])
            candidates.append(item)

    
    rerank_pairs = [(user_question, item["fulltext_summary"]) for item in candidates]
    scores = reranker.predict(rerank_pairs)

    for i, item in enumerate(candidates):
        item["rerank_score"] = float(scores[i])

    
    sorted_candidates = sorted(candidates, key=lambda x: x["rerank_score"], reverse=True)

    
    final_results = []
    for item in sorted_candidates:
        if item["similarity"] >= threshold:
            final_results.append({
                "answers": item["answers_summary"],
                "url": item.get("question_url"),
                "similarity": round(item["similarity"], 3),
                "rerank_score": round(item["rerank_score"], 3)
            })

    
    if not final_results:
        return [{
            "answers": "No relevant legal advice found for your query.",
            "url": None,
            "similarity": 0,
            "rerank_score": 0
        }]

    return final_results
