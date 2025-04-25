# core_llm/interpreter.py

from core_llm.local_engine import query_local_llm
from core_llm.gpt4_fallback import query_gpt4

def interpret(prompt, temperature=0.7):
    """
    Reçoit une requête texte, tente une réponse via LM Studio.
    En cas d'échec, utilise GPT-4 en fallback.
    """
    messages = [{"role": "user", "content": prompt}]

    # 1. On tente le modèle local
    local_response = query_local_llm(messages, temperature=temperature)

    if "[ERREUR LOCAL_LLM]" not in local_response:
        return local_response.strip()

    # 2. Fallback vers GPT-4
    gpt4_response = query_gpt4(messages, temperature=temperature)
    return gpt4_response.strip()
