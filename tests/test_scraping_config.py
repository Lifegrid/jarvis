import json

def test_scraping_sources():
    with open("config/scraping_sources.json", "r", encoding="utf-8") as f:
        data = json.load(f)
    
    print("✅ Sources trouvées :", len(data["sources"]))
    for src in data["sources"]:
        print(f"🔹 {src['name']} – Catégorie : {src['category']} – Scrapable à la demande : {src['scrapable_on_demand']}")

if __name__ == "__main__":
    test_scraping_sources()
