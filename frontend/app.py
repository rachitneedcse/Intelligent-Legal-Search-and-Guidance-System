import streamlit as st
import requests

st.title("⚖️ Legal Chatbot")

backend_url = "http://localhost:8000/chat"

query = st.text_input("Ask your legal question:")

if st.button("Get Response"):
    if not query.strip():
        st.warning("Please enter a question.")
    else:
        payload = {"query": query}
        response = requests.post(backend_url, json=payload)

        if response.status_code == 200:
            data = response.json()
            result = data["result"]

            st.subheader("📘 Legal Context (RAG)")
            rag = result.get("rag_output")

            # -------------------------------
            # 1️⃣ Handle RAG Types Correctly
            # -------------------------------

            if isinstance(rag, dict) and rag.get("type") == "Q&A Match":
                st.write(f"**Matched Question:** {rag['question']}")
                st.write(f"**Similarity:** {rag['similarity']}")
                st.write(f"**Answer:** {rag['answer']}")

            elif isinstance(rag, dict) and rag.get("type") == "RAG Generation":
                st.write(f"**Similarity:** {rag['similarity']}")
                st.write("**Generated Legal Explanation:**")
                st.write(rag["generated_answer"])

            elif isinstance(rag, dict) and rag.get("type") == "No Match":
                st.write("❌ No matching legal context found.")
                st.write(f"Similarity: {rag['similarity']}")

            else:
                st.write("⚠️ Unexpected RAG output format.")
                st.write(rag)

            # -------------------------------
            # 2️⃣ Advice Summary
            # -------------------------------
            st.subheader("📝 Retrieved Legal Advice Summary")
            st.write(result.get("advice_summary", "Not available."))

            # -------------------------------
            # 3️⃣ Advice Source URL
            # -------------------------------
            if result.get("url"):
                st.subheader("🔗 Source Link")
                st.write(result["url"])

            # -------------------------------
            # 4️⃣ Similarity & Rerank Scores
            # -------------------------------
            st.write(f"📊 Similarity Score: {result.get('similarity')}")
            st.write(f"🔍 Rerank Score: {result.get('rerank_score')}")

            # -------------------------------
            # 5️⃣ Optional: AI-Generated Advice
            # -------------------------------
            if result.get("generated_advice"):
                st.subheader("💬 AI-Generated Practical Advice")
                st.write(result["generated_advice"])

        else:
            st.error("❌ Backend not responding! Check if FastAPI is running.")
