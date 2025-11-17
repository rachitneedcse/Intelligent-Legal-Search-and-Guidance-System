# backend/scripts/prepare_advice_data.py
import json, os

RAW_PATH = "backend/data/answers_data.json"
OUTPUT_PATH = "backend/data/processed_lawyer_data.json"

print("🔹 Loading raw legal advice dataset...")
with open(RAW_PATH, "r", encoding="utf-8") as f:
    data = json.load(f)

processed_data = []
for entry in data:
    full_text = entry["full_text"]
    answers = entry["answers"]
    question_url = entry["question_url"]

    joined_answers = "\n".join(answers)
    processed_data.append({
        "question_url": question_url,
        "full_text": full_text,
        "joined_answers": joined_answers
    })

os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
    json.dump(processed_data, f, indent=2, ensure_ascii=False)
print(f"✅ Saved cleaned dataset to {OUTPUT_PATH}")
