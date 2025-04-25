import os
from core.llm_interface import call_llm  # Assure-toi que ce module est présent dans /core/

def summarize_txt_file(path: str) -> str:
    """Lit un fichier texte brut et en fait un résumé via LLM"""
    if not os.path.exists(path):
        return "[Erreur] Fichier introuvable."

    try:
        with open(path, "r", encoding="utf-8") as f:
            content = f.read()

        if len(content.strip()) == 0:
            return "[Info] Le fichier est vide."

        # On tronque pour éviter les prompts trop longs (ex: 8000 tokens max)
        if len(content) > 6000:
            content = content[:6000] + "\n... (contenu tronqué)"

        prompt = (
            "Voici un document texte brut. Résume son contenu de façon claire et structurée.\n\n"
            f"{content}"
        )

        résumé = call_llm(prompt)
        return résumé.strip()

    except Exception as e:
        return f"[Erreur lecture fichier] {str(e)}"

# Test CLI
if __name__ == "__main__":
    path = "data/raw/montexte.md"
    résumé = summarize_txt_file(path)
    print(résumé)
