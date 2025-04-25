import requests
from bs4 import BeautifulSoup
from core_llm.llm_client import chat_with_llm


def summarize_content(html):
    try:
        soup = BeautifulSoup(html, "html.parser")
        text = soup.get_text()

        prompt = (
            "Résume le contenu suivant de manière concise et claire :\n"
            f"{text[:4000]}"
        )

        response = chat_with_llm(prompt)

        # Vérification défensive de la structure de réponse
        if isinstance(response, dict) and "choices" in response:
            return response["choices"][0]["message"]["content"]
        elif isinstance(response, str):
            return response  # Si LLM renvoie juste un texte brut
        else:
            return "[Erreur LLM] Réponse inattendue : " + str(response)

    except Exception as e:
        return f"[Erreur résumé] {str(e)}"
