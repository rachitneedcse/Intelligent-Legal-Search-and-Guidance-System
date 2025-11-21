<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>Legal Chatbot README</title>
<style>
    body { font-family: Arial, sans-serif; line-height: 1.6; padding: 20px; }
    code { background: #f4f4f4; padding: 4px; border-radius: 4px; }
    pre { background: #f4f4f4; padding: 10px; border-radius: 6px; }
    h1, h2, h3 { color: #222; }
</style>
</head>
<body>

<h1>Legal Chatbot – AI-Powered Indian Law Assistant</h1>
<h3>FastAPI Backend • Streamlit Frontend • RAG • Legal Advice Retrieval • Fine-Tuned INLegalBERT • FAISS • BART Summarization</h3>

<hr>

<h2>Overview</h2>
<p>
This project is a full-stack AI legal assistant for Indian law queries. It includes:
</p>

<ul>
    <li>Retrieval-Augmented Generation (RAG)</li>
    <li>Legal advice retrieval (FAISS + CrossEncoder)</li>
    <li>Fine-tuned INLegalBERT embeddings</li>
    <li>BART summarization pipeline</li>
    <li>FastAPI backend</li>
    <li>Streamlit frontend</li>
</ul>

<p>
The system returns legal context, summarized advice, URLs, scores, and optional generated guidance.
</p>

<hr>

<h2>Features</h2>
<ul>
    <li>Section-based legal reasoning using RAG</li>
    <li>Real lawyer advice retrieval</li>
    <li>Summarized Q&A for fine-tuning</li>
    <li>INLegalBERT embedding model</li>
    <li>FAISS search + CrossEncoder reranking</li>
    <li>Modular backend</li>
    <li>Streamlit-based frontend UI</li>
</ul>

<hr>

<h2>Project Structure</h2>

<pre>
legal_chat_bot/
│
├── backend/
│   ├── main.py
│   ├── rag_module.py
│   ├── advice_module.py
│   ├── models/
│   │   └── inlegalbert_model.py
│   ├── data/
│   │   ├── processed_lawyer_data.json
│   │   ├── summarized_legal_data.json
│   │   ├── legal_chunks.npy
│   │   ├── legal_embeddings.npy
│   │   ├── question_embeddings.pt
│   │   └── faiss_index/
│   ├── scripts/
│   │   ├── build_legal_chunks.py
│   │   ├── build_question_embeddings.py
│   │   ├── build_advice_summaries.py
│   │   ├── fine_tune_inlegalbert.py
│   │   └── build_advice_index.py
│
├── frontend/
│   └── app.py
│
├── .gitignore
└── README.md
</pre>

<hr>

<h2>Installation</h2>

<h3>1. Clone the repository</h3>
<pre><code>git clone https://github.com/yourusername/legal_chat_bot.git
cd legal_chat_bot
</code></pre>

<h3>2. Create a virtual environment</h3>
<pre><code>python -m venv venv
venv\Scripts\activate     # Windows
# OR
source venv/bin/activate  # Linux / Mac
</code></pre>

<h3>3. Install dependencies</h3>
<pre><code>pip install -r requirements.txt
</code></pre>

<h3>4. Add API Key</h3>
<p>Create a <code>.env</code> file:</p>

<pre><code>TOGETHER_API_KEY=your_api_key_here
</code></pre>

<hr>

<h2>Running the Backend (FastAPI)</h2>

<pre><code>uvicorn backend.main:app --reload
</code></pre>

<p>Swagger UI:</p>
<a href="http://localhost:8000/docs">http://localhost:8000/docs</a>

<hr>

<h2>Running the Frontend (Streamlit)</h2>

<pre><code>streamlit run frontend/app.py
</code></pre>

<p>Runs at:</p>
<a href="http://localhost:8501">http://localhost:8501</a>

<hr>

<h2>Full Pipeline</h2>

<h3>1. Summarize Q&A</h3>
<pre><code>python backend/scripts/build_advice_summaries.py
</code></pre>

<h3>2. Fine-Tune INLegalBERT</h3>
<pre><code>python backend/scripts/fine_tune_inlegalbert.py
</code></pre>

<h3>3. Build FAISS Index</h3>
<pre><code>python backend/scripts/build_advice_index.py
</code></pre>

<h3>4. Build RAG Legal Chunks</h3>
<pre><code>python backend/scripts/build_legal_chunks.py
</code></pre>

<h3>5. Build Question Embeddings</h3>
<pre><code>python backend/scripts/build_question_embeddings.py
</code></pre>

<hr>

<h2>API Reference</h2>

<h3>POST /chat</h3>

<p><strong>Request:</strong></p>
<pre><code>{
  "query": "My wife is forcing me to sign divorce papers"
}
</code></pre>

<p><strong>Response:</strong></p>
<pre><code>{
  "query": "...",
  "result": {
    "rag_output": { ... },
    "advice_summary": "...",
    "url": "...",
    "similarity": 0.94,
    "rerank_score": -8.8,
    "generated_advice": "..."
  }
}
</code></pre>

<h3>POST /advice</h3>
<p>Returns only the advice retrieval results.</p>

<hr>

<h2>Tech Stack</h2>

<ul>
    <li>Python</li>
    <li>FastAPI</li>
    <li>Streamlit</li>
    <li>SentenceTransformers</li>
    <li>INLegalBERT</li>
    <li>BART Large</li>
    <li>FAISS</li>
    <li>CrossEncoder</li>
    <li>Together API</li>
</ul>

<hr>

<h2>Roadmap</h2>
<ul>
    <li>Chat history</li>
    <li>Nearby legal centers using city input</li>
    <li>Docker deployment</li>
    <li>Hindi / multilingual support</li>
    <li>Local LLM support</li>
</ul>

<hr>



</body>
</html>
