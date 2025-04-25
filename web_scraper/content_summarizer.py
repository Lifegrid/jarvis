from core_llm.llm_client import chat_with_llm

def summarize_content(text):
    try:
        prompt = f"Voici un contenu extrait d’une page web :\n\n{text}\n\nPeux-tu le résumer en quelques lignes ?"
        summary = chat_with_llm(prompt)
        return summary
    except Exception as e:
        return f"[Erreur résumé] {e}"
