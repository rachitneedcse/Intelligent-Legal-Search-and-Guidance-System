<h1>⚖️ LegalChatBot</h1>
<p>
A Retrieval-Augmented Generation (RAG) based chatbot designed for the Indian legal system.<br>
It not only retrieves law-related content but also provides location-based resources and lawyer advice.<br>
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
LegalChatBot.ipynb          # Main development notebook

# Summarization & Models
bart_summarizer/            # Summarization checkpoints
checkpoints/                # Training checkpoints
fine-tuned-inlegalbert/     # Fine-tuned INLegalBERT model
legal_model/                # Trained legal model
qa_model/                   # Question-answer model

# Input Datasets
crpc-india/                 # CRPC QA dataset
final-database/             # Final law database JSON
indian-law/                 # Indian legal PDFs (Constitution, IPC, Acts, etc.)
legal-advice/               # Lawyer Q&A data

# Processed Data & Indexes
full_texts.json             # Raw full-text data
final_summarized_data.json  # Summarized dataset
summarized_legal_data.json  # Alternate summarized data
processed_lawyer_data.json  # Processed lawyer advice

legal_chunks.npy            # Pre-chunked text for embeddings
legal_embeddings.npy        # Embedding vectors
legal_faiss.index           # FAISS index for retrieval
final_faiss_fulltext.index  # Alternate full-text FAISS index
question_embeddings.pt      # Embeddings of user/legal questions

# Misc
state.db                    # Local database state
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







<hr>


<h2>⚠️ Disclaimer</h2>
<p>
This project is built <b>for research and educational purposes only</b>.  
It is <b>not a substitute for professional legal advice</b>.  
While the system retrieves laws, documents, and lawyer experiences, its responses may be incomplete, outdated, or inaccurate.  
Always consult a <b>qualified legal professional</b> for any real-world legal matters.  
</p>

<hr>

<h2>🤝 Contributing</h2>
<p>Pull requests and issues welcome.<br>
Do not upload large datasets or models; link them instead.</p>

<hr>

<h2>📜 License</h2>
<p>Add a <code>LICENSE</code> file (e.g., MIT).</p>
