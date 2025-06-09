# ────────────────────────────────
# 📥 ingestion/file_loader.py
# ────────────────────────────────
import fitz  # PyMuPDF
import json

def load_file(path):
    if path.endswith(".pdf"):
        with fitz.open(path) as doc:
            return "\n".join(page.get_text() for page in doc)
    elif path.endswith(".json"):
        with open(path, 'r') as f:
            return json.dumps(json.load(f))
    elif path.endswith(".txt"):
        with open(path, 'r') as f:
            return f.read()
    else:
        raise ValueError("Unsupported file format")