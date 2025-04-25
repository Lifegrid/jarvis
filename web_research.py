import requests
from bs4 import BeautifulSoup
from duckduckgo_search import DDGS
from web_memory import store_web_memory

def search_web(query: str, max_results: int = 5) -> list[dict]:
    with DDGS() as ddgs:
        return list(ddgs.text(query, max_results=max_results))

def extract_summary_from_url(url: str) -> str:
    try:
        response = requests.get(url, timeout=10)
        soup = BeautifulSoup(response.text, 'html.parser')
        paragraphs = soup.find_all('p')
        text = ' '.join(p.get_text() for p in paragraphs[:10])
        return text.strip()
    except Exception as e:
        return f"Erreur lors de l'extraction : {e}"

def autonomous_web_research(query: str) -> str:
    results = search_web(query)
    summaries = []
    for res in results[:3]:
        title = res.get("title", "Sans titre")
        href = res.get("href") or res.get("url")
        if href:
            content = extract_summary_from_url(href)
            summaries.append(f"🔗 {title} ({href}):\n{content}\n")
    return "\n\n".join(summaries) if summaries else "Aucun résultat pertinent trouvé."

def perform_web_research(query: str, max_results: int = 5) -> str:
    results = search_web(query, max_results)
    return "\n".join([f"- {r['title']}: {r['href']}" for r in results if r.get('title') and r.get('href')])

# Détection simple si un message nécessite une recherche web
def needs_web_search(message: str) -> bool:
    triggers = ["cherche", "recherche", "trouve", "infos sur", "c'est quoi", "qui est", "comment faire", "prix", "derniers", "résultats", "actuel", "cours"]
    return any(word in message.lower() for word in triggers)
