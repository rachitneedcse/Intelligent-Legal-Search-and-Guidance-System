<h1>⚖️ LegalChatBot</h1>
<p>
A Retrieval-Augmented Generation (RAG) based chatbot designed for the Indian legal system.<br>
It not only retrieves law-related content but also provides location-based resources and lawyer advice.<br>
⚠️ This tool provides <b>legal information, not legal advice</b>.
</p>

<hr>

<h2>✨ Key Features (What Makes It Unique)</h2>
<ol>
  <li><b>Legal Knowledge Retrieval (RAG)</b>: Retrieve any information about the Indian law system using a RAG pipeline (SentenceTransformer embeddings + FAISS search + reranking).</li>
  <img width="1231" height="397" alt="Screenshot 2025-08-14 220806" src="https://github.com/user-attachments/assets/19add1c2-9463-4ed1-8f09-556fdb5805bc" />

  <li><b>Location Awareness</b>: Get nearby firms, lawyers, and judicial landmarks based on your city or location.</li>
  <img width="915" height="299" alt="Screenshot 2025-08-14 220840" src="https://github.com/user-attachments/assets/9047fb88-d1fd-4724-ac91-f9054d82611f" />

  <li><b>Real Lawyer Insights</b>: Access actual Indian lawyer advice and related experiences matched to your question context.</li>
  <img width="1395" height="779" alt="Screenshot 2025-08-14 220930" src="https://github.com/user-attachments/assets/6122ce62-eb81-43a2-9762-3e290a51ceae" />

</ol>

<hr>

<h2>📦 Project Layout</h2>
<pre>
LegalChatBot.ipynb      # Main development notebook
input_data/             # Small configs/sample data
data/                   # Raw sources (JSON/CSV/PDF) - large files excluded
faiss_index/            # Saved FAISS indexes
models/                 # Saved/finetuned models (do not commit large weights)
</pre>

<hr>

<h2>🧰 Dependencies</h2>
<ul>
  <li>python ≥ 3.10</li>
  <li>torch, transformers</li>
  <li>sentence-transformers</li>
  <li>faiss-cpu</li>
  <li>langchain</li>
  <li>pypdf / PyPDF2</li>
  <li>pandas, numpy</li>
  <li>together (API client)</li>
</ul>

<pre>
pip install torch transformers sentence-transformers \
    faiss-cpu langchain pypdf pandas numpy together
</pre>

<hr>

<h2>⚙️ Configuration</h2>
<pre>
# Linux / macOS
export TOGETHER_API_KEY="YOUR_KEY"

# Windows (PowerShell)
$env:TOGETHER_API_KEY="YOUR_KEY"
</pre>

<hr>

<h2>🚀 Quick Start</h2>
<ol>
  <li>Clone the repo and install dependencies</li>
  <li>Place legal datasets (JSON/CSV/PDF) locally or on Kaggle</li>
  <li>Open and run <code>LegalChatBot.ipynb</code></li>
</ol>

<pre>
query = "What is the process to file a cybercrime complaint in Delhi?"

# Steps:
# 1) Embed query
# 2) Search FAISS
# 3) Rerank
# 4) Summarize (optional)
# 5) Generate final answer via Together API
</pre>

<hr>

<h2>🧠 How It Works</h2>
<ol>
  <li><b>Load Data</b>: JSON/CSV/PDF sources of Indian laws and legal Q&A</li>
  <li><b>Embed</b>: Encode chunks with SentenceTransformer (e.g., INLegalBERT-based)</li>
  <li><b>Index</b>: Store embeddings in FAISS for fast retrieval</li>
  <li><b>Retrieve</b>: Find top-k most relevant sections for a user’s question</li>
  <li><b>Rerank</b>: Use CrossEncoder to boost precision</li>
  <li><b>Summarize</b>: Use BART-large for long passages (optional)</li>
  <li><b>Generate</b>: Final answer crafted using Together API, enriched with lawyer advice & location context</li>
</ol>

<hr>

<h2>📁 Example Datasets</h2>
<pre>
/kaggle/input/crpc-india/crpc_qa.json
/kaggle/input/final-database/legal_database.json
/kaggle/input/indian-law/COI.pdf
/kaggle/input/legal-advice/answers_data.json
</pre>

<hr>

<h2>🔒 Security & Safety</h2>
<ul>
  <li>Never commit API keys (use <code>.env</code> or environment variables)</li>
  <li>Responses are <b>informational only</b></li>
  <li>Validate sources and add citations wherever possible</li>
</ul>

<hr>

<h2>🧭 Limitations</h2>
<ul>
  <li>May miss latest amendments or case law without refreshed data</li>
  <li>Location services depend on accurate city-level input</li>
  <li>Lawyer advice is summarized and not a substitute for professional consultation</li>
</ul>

<hr>

<h2>🤝 Contributing</h2>
<p>Pull requests and issues welcome.<br>
Do not upload large datasets or models; link them instead.</p>

<hr>

<h2>📜 License</h2>
<p>Add a <code>LICENSE</code> file (e.g., MIT).</p>
