import qrcode
import os
from datetime import datetime

def generate_qr_code(content: str, save_path: str = "data/summaries/") -> str:
    """Crée un QR code à partir d’un texte ou lien et l’enregistre"""
    if not content or len(content.strip()) == 0:
        return "[Erreur] Aucun contenu fourni pour générer le QR code."

    try:
        img = qrcode.make(content)
        filename = f"qr_{datetime.now().strftime('%Y%m%d_%H%M%S')}.png"
        full_path = os.path.join(save_path, filename)

        os.makedirs(save_path, exist_ok=True)
        img.save(full_path)

        return f"[QR] QR code généré : {full_path}"
    
    except Exception as e:
        return f"[Erreur QR] {str(e)}"

# Test CLI
if __name__ == "__main__":
    result = generate_qr_code("https://jarvis.ai")
    print(result)
