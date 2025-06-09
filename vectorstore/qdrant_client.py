# ────────────────────────────────
# 📦 vectorstore/qdrant_client.py
# ────────────────────────────────
from qdrant_client import QdrantClient
from configs.settings import QDRANT_URL, QDRANT_API_KEY

qdrant_client = QdrantClient(
    url=QDRANT_URL,
    api_key=QDRANT_API_KEY
)
