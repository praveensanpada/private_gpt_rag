# ────────────────────────────────
# 📦 vectorstore/embed_store.py
# ────────────────────────────────
from sentence_transformers import SentenceTransformer
from qdrant_client.models import Distance, VectorParams, PointStruct
from .qdrant_client import qdrant_client as client
import uuid

model = SentenceTransformer('all-MiniLM-L6-v2')

try:
    client.recreate_collection(
        collection_name="private_gpt",
        vectors_config=VectorParams(size=384, distance=Distance.COSINE),
    )
except Exception as e:
    print("⚠️ Could not connect to Qdrant:", e)

def store_chunks(chunks):
    vectors = model.encode(chunks).tolist()
    points = [
        PointStruct(id=str(uuid.uuid4()), vector=v, payload={"text": t})
        for t, v in zip(chunks, vectors)
    ]
    client.upsert(collection_name="private_gpt", points=points)