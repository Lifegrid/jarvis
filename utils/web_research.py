from duckduckgo_search import DDGS

def perform_web_research(query: str) -> str:
    results = []
    try:
        with DDGS() as ddgs:
            for r in ddgs.text(query, max_results=5):
                results.append(f"- {r['title']} : {r['href']}")
    except Exception as e:
        return f"❌ Erreur lors de la recherche web : {str(e)}"

    if not results:
        return "Aucun résultat pertinent trouvé."

    return f"🔍 Résultats Web pour « {query} » :\n" + "\n".join(results)
