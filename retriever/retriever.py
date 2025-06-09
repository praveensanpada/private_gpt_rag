# ────────────────────────────────
# 🔍 retriever/retriever.py
# ────────────────────────────────
from sentence_transformers import SentenceTransformer
from vectorstore.qdrant_client import qdrant_client as client

model = SentenceTransformer('all-MiniLM-L6-v2')

def retrieve(query):
    query_vec = model.encode([query])[0].tolist()
    results = client.search(collection_name="private_gpt", query_vector=query_vec, limit=5)
    return [r.payload['text'] for r in results]