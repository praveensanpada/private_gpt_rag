# ────────────────────────────────
# 🚪 app.py
# ────────────────────────────────
import streamlit as st
from ingestion.file_loader import load_file
from ingestion.chunker import chunk_text
from vectorstore.embed_store import store_chunks
from retriever.retriever import retrieve
from llm.openai_interface import ask_openai

st.title("Private GPT")

uploaded = st.file_uploader("Upload PDF, TXT, or JSON", type=["pdf", "txt", "json"])
question = st.text_input("Ask a question")

if uploaded and question:
    with open(f"temp_{uploaded.name}", "wb") as f:
        f.write(uploaded.read())

    raw_text = load_file(f.name)
    chunks = chunk_text(raw_text)
    store_chunks(chunks)

    context = "\n".join(retrieve(question))
    answer = ask_openai(context, question)
    st.write("### Answer")
    st.write(answer)
