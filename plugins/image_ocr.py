import pytesseract
from PIL import Image
import os

def extract_text_from_image(image_path: str) -> str:
    """Utilise Tesseract pour lire le texte d'une image"""
    if not os.path.exists(image_path):
        return "[Erreur] Fichier introuvable."

    try:
        image = Image.open(image_path)
        text = pytesseract.image_to_string(image)
        return text.strip() if text else "[Info] Aucun texte détecté dans l’image."
    except Exception as e:
        return f"[Erreur OCR] {str(e)}"

# Test CLI
if __name__ == "__main__":
    path = "data/raw/exemple.png"
    texte = extract_text_from_image(path)
    print(texte)
