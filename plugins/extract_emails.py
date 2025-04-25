import re
import os

def extract_emails_from_file(path: str) -> list:
    """Détecte toutes les adresses email dans un fichier texte"""
    if not os.path.exists(path):
        return ["[Erreur] Fichier introuvable."]

    try:
        with open(path, "r", encoding="utf-8") as f:
            content = f.read()

        pattern = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"
        emails = re.findall(pattern, content)
        return list(set(emails)) or ["[Info] Aucune adresse email trouvée."]
    
    except Exception as e:
        return [f"[Erreur de lecture] {str(e)}"]

# Test CLI
if __name__ == "__main__":
    path = "data/raw/contact.txt"
    emails = extract_emails_from_file(path)
    print("\n".join(emails))
