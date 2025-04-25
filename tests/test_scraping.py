from web_scraper.web_navigator import fetch_page_content
from web_scraper.page_reader import extract_main_content
from web_scraper.source_vectorizer import store_vector
from memory_engine.memory_search import search_memory

def test_scraping_flow():
    url = "https://fr.wikipedia.org/wiki/Intelligence_artificielle"
    
    print("🌐 Étape 1 : Récupération de la page...")
    html = fetch_page_content(url)
    assert "Intelligence artificielle" in html or "<html" in html.lower()
    print("✅ Page récupérée.")

    print("📖 Étape 2 : Extraction et résumé du contenu...")
    content = extract_main_content(html)
    print("📄 Résumé extrait :")
    print(content[:500] + "..." if len(content) > 500 else content)
    assert len(content) > 100

    print("💾 Étape 3 : Stockage vectoriel...")
    store_vector(url, content)
    print("✅ Stocké dans la mémoire.")

    print("🔍 Étape 4 : Recherche mémoire...")
    results = search_memory("qu'est-ce que l'intelligence artificielle ?")
    print("🧠 Résultats de recherche :")
    for doc in results:
        print("-", doc[:200].replace("\\n", " "), "...\n")

if __name__ == "__main__":
    test_scraping_flow()
