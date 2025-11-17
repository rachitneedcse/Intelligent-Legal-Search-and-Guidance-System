import os, json
import torch
from sentence_transformers import SentenceTransformer, models, losses, InputExample
from torch.utils.data import DataLoader

DATA_PATH = "backend/data/summarized_legal_data.json"
OUTPUT_PATH = "backend/models/fine_tuned_inlegalbert"
MODEL_NAME = "law-ai/InLegalBERT"

EPOCHS = 3
BATCH_SIZE = 4
MAX_SEQ_LENGTH = 512

device = "cuda" if torch.cuda.is_available() else "cpu"
print(f"🧠 Using device: {device}")

print("🔹 Loading summarized data...")
with open(DATA_PATH, "r", encoding="utf-8") as f:
    data = json.load(f)

if not data:
    raise ValueError("❌ No data found in summarized_legal_data.json")

train_examples = [
    InputExample(texts=[item["fulltext_summary"], item["answers_summary"]], label=1)
    for item in data
]
print(f"✅ Loaded {len(train_examples)} training examples")

word_embedding_model = models.Transformer(MODEL_NAME, max_seq_length=MAX_SEQ_LENGTH)
pooling_model = models.Pooling(word_embedding_model.get_word_embedding_dimension())
model = SentenceTransformer(modules=[word_embedding_model, pooling_model]).to(device)


train_dataloader = DataLoader(train_examples, shuffle=True, batch_size=BATCH_SIZE)
train_loss = losses.CosineSimilarityLoss(model=model)

os.environ["WANDB_DISABLED"] = "true"

print("🧠 Fine-tuning InLegalBERT...")
model.fit(
    train_objectives=[(train_dataloader, train_loss)],
    epochs=EPOCHS,
    warmup_steps=100,
    show_progress_bar=True
)

os.makedirs(OUTPUT_PATH, exist_ok=True)
model.save(OUTPUT_PATH)
print(f"✅ Fine-tuned model saved to: {OUTPUT_PATH}")
