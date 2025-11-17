

from fastapi import FastAPI
from pydantic import BaseModel
from backend.rag_module import get_answer
from backend.advice_module import get_legal_advice

app = FastAPI(title="Legal Chatbot API", version="1.0")


class QueryRequest(BaseModel):
    query: str


@app.get("/")
def home():
    return {"message": "Welcome to the Legal Chatbot API"}


@app.post("/chat")
def chat_endpoint(request: QueryRequest):
    """
    Combined RAG + Legal Advice endpoint.
    Returns both section-based law retrieval and summarized advice.
    """
    user_query = request.query.strip()

    
    try:
        rag_result = get_answer(user_query)
    except Exception as e:
        rag_result = f"❌ Error in RAG module: {e}"

    
    try:
        advice_results = get_legal_advice(user_query, top_k=3)
        if advice_results:
            best_advice = advice_results[0]
        else:
            best_advice = {"generated_advice": "No relevant advice found."}
    except Exception as e:
        best_advice = {"generated_advice": f"❌ Error in Advice module: {e}"}

    
    return {
        "query": user_query,
        "result": {
            "rag_output": rag_result,
            "advice_summary": best_advice.get("answers"),
            "url": best_advice.get("url"),
            "similarity": best_advice.get("similarity"),
            "rerank_score": best_advice.get("rerank_score"),
            "generated_advice": best_advice.get("generated_advice"),
        },
    }


@app.post("/advice")
def advice_endpoint(request: QueryRequest):
    """
    Retrieves summarized legal advice only (without full RAG).
    """
    user_query = request.query.strip()
    try:
        responses = get_legal_advice(user_query, top_k=3)
        return {"query": user_query, "results": responses}
    except Exception as e:
        return {"error": str(e)}
