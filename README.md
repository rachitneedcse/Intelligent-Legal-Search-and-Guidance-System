<!DOCTYPE html>
<html lang="en">
<head></head>
<body>

<h1>Legal Chatbot – AI-Powered Indian Law Assistant</h1>
<h3>FastAPI Backend • Streamlit Frontend • Legal Knowledge Retrieval • Legal Advice Retrieval • Location-Based Assistance</h3>

<hr>

<h2>Overview</h2>

<p>
This project is a full-stack <strong>AI Legal Chatbot</strong> designed to assist users with questions related to Indian law.  
It combines <strong>Retrieval-Augmented Generation (RAG)</strong>, <strong>real lawyer advice retrieval</strong>, and <strong>location-based legal assistance</strong> to give users both legal context and practical solutions.
</p>

<p>
The system is built with:
</p>

<ul>
    <li>FastAPI backend</li>
    <li>Streamlit frontend</li>
    <li>Fine-tuned INLegalBERT embeddings</li>
    <li>FAISS vector search for fast retrieval</li>
    <li>BART summarization for compressing legal Q&A</li>
    <li>Mistral-7B (Together API) for generating legal explanations</li>
</ul>

<hr>

<h2>Key Functionalities</h2>

<h3>1️⃣ Legal Knowledge Retrieval (RAG)</h3>
<p>
This module provides <strong>law-based explanations</strong> using IPC, HMA, CrPC, and other statutes.  
It retrieves relevant legal text using FAISS and generates a <strong>5-point structured legal answer</strong> using Mistral-7B.
</p>

<h4>Capabilities:</h4>
<ul>
    <li>Finds the correct legal section</li>
    <li>Explains punishment, exceptions, and applicability</li>
    <li>Gives concise and structured legal summaries</li>
</ul>

<hr>

<h3>2️⃣ Legal Advice Retrieval (Real Lawyer Answers)</h3>
<p>
This system retrieves <strong>real lawyer-provided advice</strong> by matching the user's question with summarized legal Q&A data.  
It uses fine-tuned INLegalBERT embeddings for semantic matching, FAISS for fast retrieval, and a CrossEncoder for precise reranking.
</p>

<h4>Provides:</h4>
<ul>
    <li>Best matching lawyer advice</li>
    <li>Advice summary</li>
    <li>Source URL of the original question</li>
    <li>Similarity score</li>
    <li>Rerank score</li>
</ul>

<hr>

<h3>3️⃣ Location-Based Legal Assistance</h3>
<p>
The system supports an optional module that helps users find:
</p>
<ul>
    <li>Lawyers</li>
    <li>Legal aid centers</li>
    <li>Police stations</li>
    <li>Court locations</li>
</ul>

<p>
This feature activates when the user provides a <strong>city name</strong> along with their query.
</p>

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
