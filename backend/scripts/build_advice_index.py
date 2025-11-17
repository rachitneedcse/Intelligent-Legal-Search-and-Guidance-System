# backend/scripts/build_advice_index.py
import json, numpy as np, faiss
from sentence_transformers import SentenceTransformer
import os
DATA_PATH = "backend/data/summarized_legal_data.json"
MODEL_PATH = "backend/models/fine_tuned_inlegalbert"
INDEX_PATH = "backend/data/faiss_index/advice_index.index"

print("🔹 Loading data and fine-tuned model...")
with open(DATA_PATH, "r",encoding="utf-8") as f:
    data = json.load(f)

model = SentenceTransformer(MODEL_PATH)
texts = [item["fulltext_summary"] for item in data]
print(f"✅ Loaded {len(texts)} summaries")

embeddings = model.encode(texts, convert_to_numpy=True, show_progress_bar=True)
faiss.normalize_L2(embeddings)

dimension = embeddings.shape[1]
index = faiss.IndexFlatIP(dimension)
index.add(embeddings)

os.makedirs(os.path.dirname(INDEX_PATH), exist_ok=True)
faiss.write_index(index, INDEX_PATH)
print(f"✅ FAISS index saved to {INDEX_PATH}")
