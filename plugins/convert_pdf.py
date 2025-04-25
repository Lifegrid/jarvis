import fitz  # PyMuPDF
import os

def convert_pdf_to_text(pdf_path: str) -> str:
    """Extrait le texte brut d’un fichier PDF (page par page)"""
    if not os.path.exists(pdf_path):
        return "[Erreur] Fichier introuvable."

    try:
        doc = fitz.open(pdf_path)
        full_text = []

        for page in doc:
            text = page.get_text()
            if text:
                full_text.append(text.strip())

        doc.close()
        return "\n\n".join(full_text) if full_text else "[Info] Aucun texte détecté dans le PDF."
    except Exception as e:
        return f"[Erreur lors de la conversion PDF] {str(e)}"

# Test CLI
if __name__ == "__main__":
    path = "data/raw/exemple.pdf"
    output = convert_pdf_to_text(path)
    print(output[:1000])  # Affiche les 1000 premiers caractères
