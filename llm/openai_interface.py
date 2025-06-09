# ────────────────────────────────
# 🤖 llm/openai_interface.py
# ────────────────────────────────
# Requires: openai>=1.14.3
# Install using:
#   pip install --upgrade openai==1.14.3

from openai import OpenAI
from configs.settings import OPENAI_API_KEY

client = OpenAI(api_key=OPENAI_API_KEY)

def ask_openai(context, question):
    prompt = f"Context:\n{context}\n\nQuestion: {question}"
    response = client.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt},
        ]
    )
    return response.choices[0].message.content