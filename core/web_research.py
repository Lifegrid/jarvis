# core/web_research.py

import requests
from bs4 import BeautifulSoup
from duckduckgo_search import DDGS
from core.llm_interface import ask_llm
from core.web_memory import store_web_memory, search_web_memory

def perform_web_research(query: str) -> str:
    """
    Fonction principale qui effectue une recherche intelligente sur le web.
    1. Cherche d'abord dans la mémoire locale
    2. Si besoin, interroge DuckDuckGo
    3. Résume les résultats de manière utile
    """

    # 1. Vérifie d'abord dans la mémoire
    cached_result = search_web_memory(query)
    if cached_result:
        return f"(🧠 Résultat de la mémoire web)\n\n{cached_result}"

    # 2. Sinon, fait une vraie recherche web
    results = []
    try:
        with DDGS() as ddgs:
            results = ddgs.text(query, safesearch="Off", region="wt-wt", max_results=5)
    except Exception as e:
        return f"❌ Erreur recherche web : {str(e)}"

    if not results:
        return "❌ Aucun résultat trouvé sur Internet."

    # 3. Récupère les pages et extrait un peu de contenu
    snippets = []
    for r in results:
        url = r.get("href")
        if url:
            text = scrape_website_text(url)
            if text:
                snippets.append(f"- [{r.get('title', 'Lien')}]({url}) : {text[:300]}...")  # Limite à 300 caractères

    if not snippets:
        return "❌ Résultats vides après scraping."

    # 4. Demande au LLM de résumer intelligemment
    prompt = (
        "Voici des extraits de sites web trouvés pour la question suivante :\n"
        f"'{query}'\n\n"
        "Synthétise ces informations en une réponse claire et concise, avec les points clés :\n\n"
        + "\n".join(snippets)
    )

    final_summary = ask_llm([
        {"role": "system", "content": "Tu es un assistant personnel qui synthétise des recherches web de façon utile, fiable, concise."},
        {"role": "user", "content": prompt}
    ])

    # 5. Stocke la synthèse dans la mémoire
    store_web_memory(query, final_summary)

    return final_summary

def scrape_website_text(url: str) -> str:
    """
    Essaie d'extraire du texte lisible depuis un site web (HTML -> texte brut).
    """
    try:
        response = requests.get(url, timeout=5)
        soup = BeautifulSoup(response.text, "html.parser")

        # Retire les balises inutiles
        for script in soup(["script", "style", "header", "footer", "nav", "aside"]):
            script.decompose()

        text = soup.get_text(separator="\n")
        lines = [line.strip() for line in text.splitlines() if line.strip()]
        cleaned_text = "\n".join(lines)

        return cleaned_text[:2000]  # limite à 2000 caractères max pour le traitement
    except Exception:
        return ""
