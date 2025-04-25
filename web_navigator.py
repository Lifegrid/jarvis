import requests
from bs4 import BeautifulSoup
from core_llm.llm_client import query_llm

def fetch_and_summarize(url: str) -> str:
    try:
        res = requests.get(url, timeout=5)
        soup = BeautifulSoup(res.text, "html.parser")
        title = soup.title.string if soup.title else ""
        paragraphs = "\n".join(p.get_text() for p in soup.find_all("p")[:5])
        content = f"Titre: {title}\n{paragraphs}"
        return query_llm([{"role": "user", "content": f"Résume ce contenu web :\n{content}"}])
    except Exception as e:
        return f"Erreur pour {url} : {e}"

def web_scan(query="outils IA 2024") -> str:
    search_urls = [
        f"https://www.google.com/search?q={query.replace(' ', '+')}"
    ]
    results = [fetch_and_summarize(url) for url in search_urls]
    return "\n\n".join(results)

