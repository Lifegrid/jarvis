# web_crawler.py
import requests
from bs4 import BeautifulSoup

def fetch_page_content(url: str) -> str:
    try:
        headers = {
            "User-Agent": "Mozilla/5.0 (compatible; JarvisBot/1.0)",
        }
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, "html.parser")
        paragraphs = soup.find_all("p")
        content = " ".join([p.get_text(strip=True) for p in paragraphs])
        return content[:2000]  # limite raisonnable
    except Exception as e:
        return f"⚠️ Erreur d’analyse de {url} : {e}"
