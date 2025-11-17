# backend/scripts/build_advice_summaries.py
import os
import pandas as pd
from transformers import BartTokenizer, BartForConditionalGeneration
from tqdm import tqdm
import torch
import re

# -------------------------------------------------------------------------
# 🔹 Paths
# -------------------------------------------------------------------------
INPUT_PATH = "backend/data/processed_lawyer_data.json"
OUTPUT_PATH = "backend/data/summarized_legal_data.json"
MODEL_PATH = "facebook/bart-large-cnn"  # or your local fine-tuned folder, e.g. backend/models/bart_summarizer

print("🔹 Loading processed data...")
df = pd.read_json(INPUT_PATH)

# -------------------------------------------------------------------------
# 🔹 Model & Tokenizer
# -------------------------------------------------------------------------
device = "cuda" if torch.cuda.is_available() else "cpu"
print(f"🧠 Using device: {device}")

model = BartForConditionalGeneration.from_pretrained(MODEL_PATH, forced_bos_token_id=0)
tokenizer = BartTokenizer.from_pretrained(MODEL_PATH)
model.eval().to(device)

# -------------------------------------------------------------------------
# 🔹 Helper — clean prompt leftovers if model copies them
# -------------------------------------------------------------------------
def clean_summary(text: str) -> str:
    if not text:
        return ""
    text = re.sub(r"You are a legal assistant.*?(Text:)?", "", text, flags=re.DOTALL)
    text = re.sub(r"Summarize the following legal situation.*?(Text:)?", "", text, flags=re.DOTALL)
    return text.strip()

# -------------------------------------------------------------------------
# 🔹 Summarization Function
# -------------------------------------------------------------------------
def summarize(text, max_input_length=1024, max_output_length=350):
    if not isinstance(text, str) or not text.strip():
        return ""

    prompt = (
        "You are a legal assistant. Summarize the following legal situation by extracting:\n"
        "- The legal dispute and its current status\n"
        "- Actions taken by the people involved\n"
        "- The legal question or help being asked\n\n"
        "Text:\n" + text
    )

    inputs = tokenizer(prompt, max_length=max_input_length, truncation=True, return_tensors="pt").to(device)
    summary_ids = model.generate(
        inputs["input_ids"],
        num_beams=6,
        max_length=max_output_length,
        min_length=120,
        no_repeat_ngram_size=3,
        length_penalty=1.2,
        early_stopping=True
    )

    output = tokenizer.decode(summary_ids[0], skip_special_tokens=True)
    return clean_summary(output)

# -------------------------------------------------------------------------
# 🔹 Main Summarization Loop
# -------------------------------------------------------------------------
df["fulltext_summary"] = ""
df["answers_summary"] = ""

for idx in tqdm(range(len(df)), desc="🧾 Summarizing legal entries"):
    try:
        full = df.loc[idx, "full_text"]
        ans = df.loc[idx, "joined_answers"]

        df.at[idx, "fulltext_summary"] = summarize(full)
        df.at[idx, "answers_summary"] = summarize(ans)
    except Exception as e:
        print(f"⚠️ Error at index {idx}: {e}")
        continue

# -------------------------------------------------------------------------
# 🔹 Save Output
# -------------------------------------------------------------------------
df.to_json(OUTPUT_PATH, orient="records", indent=2, force_ascii=False)
print(f"✅ Saved summarized dataset to {OUTPUT_PATH}")
