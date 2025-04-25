import requests
import os
from datetime import datetime
from urllib.parse import urlparse

def download_page_html(url: str, save_path: str = "data/raw/") -> str:
    """Télécharge la page HTML d’une URL et la sauvegarde"""
    try:
        response = requests.get(url, timeout=8)
        response.raise_for_status()

        domain = urlparse(url).netloc.replace(".", "_")
        timestamp = datetime.now().strftime("%Y%m%d_%H%M")
        filename = f"{domain}_{timestamp}.html"
        full_path = os.path.join(save_path, filename)

        os.makedirs(save_path, exist_ok=True)
        with open(full_path, "w", encoding="utf-8") as f:
            f.write(response.text)

        return f"[OK] Page téléchargée : {full_path}"
    
    except Exception as e:
        return f"[Erreur téléchargement] {str(e)}"

# Test CLI
if __name__ == "__main__":
    result = download_page_html("https://example.com")
    print(result)
