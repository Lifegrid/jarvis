import re
import os

def extract_links_from_file(path: str) -> list:
    """Détecte toutes les URLs dans un fichier texte, markdown ou HTML"""
    if not os.path.exists(path):
        return ["[Erreur] Fichier introuvable."]

    try:
        with open(path, "r", encoding="utf-8") as f:
            content = f.read()

        url_pattern = r"https?://[^\s\)\]\}\>\"']+"
        links = re.findall(url_pattern, content)

        return list(set(links)) or ["[Info] Aucun lien détecté."]
    
    except Exception as e:
        return [f"[Erreur] {str(e)}"]

# Test CLI
if __name__ == "__main__":
    path = "data/raw/texte_lien.md"
    liens = extract_links_from_file(path)
    print("\n".join(liens))
