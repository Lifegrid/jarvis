import os
import easyocr
import cv2

reader = easyocr.Reader(['fr', 'en'], gpu=True)

def analyze_image(path: str) -> str:
    """Analyse une image : OCR + résumé du contenu détecté"""
    if not os.path.exists(path):
        return "[Erreur] Image introuvable."

    try:
        result = reader.readtext(path, detail=0)
        if not result:
            return "[Jarvis Vision] Aucun texte détecté."

        extracted = "\n".join(result)
        return f"**Texte détecté dans l’image :**\n{extracted}"
    
    except Exception as e:
        return f"[Erreur OCR] {str(e)}"

# Test CLI
if __name__ == "__main__":
    output = analyze_image("data/images/test_affiche.png")
    print(output)
