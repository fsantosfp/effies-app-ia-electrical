import requests
import os

OLLAMA_URL = os.getenv("OLLAMA_URL", "http://localhost:11434/api/generate")

def chat_with_ollama(prompt: str, model: str = "gemma:7b"):
    response = requests.post(
        OLLAMA_URL,
        json={
            "model": model,
            "prompt": prompt,
            "stream": False
        }
    )

    if response.status_code == 200:
        data = response.json()
        return data["response"]
    else:
        raise Exception(f"Ollama returned error: {response.status_code} - {response.text}")
