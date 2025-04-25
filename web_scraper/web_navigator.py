import requests
from bs4 import BeautifulSoup

def fetch_page_content(url):
    try:
        headers = {"User-Agent": "Mozilla/5.0"}
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
        return response.text
    except requests.RequestException as e:
        return f"Erreur lors de la récupération de la page : {e}"
