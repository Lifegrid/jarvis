# core_llm/local_engine.py

import requests

LM_STUDIO_URL = "http://localhost:1234/v1/chat/completions"
LOCAL_MODEL = "mistral-7b-instruct-v0.3"

def query_local_llm(messages, temperature=0.7):
    """
    Envoie une requête à LM Studio avec une liste de messages.
    Retourne le texte de la réponse du modèle local.
    """
    try:
        response = requests.post(
            LM_STUDIO_URL,
            headers={"Content-Type": "application/json"},
            json={
                "model": LOCAL_MODEL,
                "messages": messages,
                "temperature": temperature
            },
            timeout=60
        )
        response.raise_for_status()
        return response.json()["choices"][0]["message"]["content"]
    except Exception as e:
        return f"[ERREUR LOCAL_LLM] {e}"
