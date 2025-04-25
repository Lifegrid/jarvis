# 📁 Chemin : auto_scrape.py

import json
from datetime import datetime, timedelta
from web_scraper.web_navigator import fetch_page_content
from web_scraper.content_summarizer import summarize_content
from web_scraper.source_vectorizer import store_vector

SCHEDULE_PATH = "config/scraping_schedule.json"


def load_schedule():
    with open(SCHEDULE_PATH, "r", encoding="utf-8") as f:
        return json.load(f)


def save_schedule(schedule):
    with open(SCHEDULE_PATH, "w", encoding="utf-8") as f:
        json.dump(schedule, f, indent=4, ensure_ascii=False)


def should_scrape(last_scraped, interval_hours):
    if not last_scraped:
        return True
    last = datetime.strptime(last_scraped, "%Y-%m-%d %H:%M:%S")
    return datetime.now() > last + timedelta(hours=interval_hours)


def auto_scrape():
    schedule = load_schedule()
    updated = False

    for source in schedule:
        name = source["name"]
        url = source["url"]
        category = source.get("category", "general")
        last_scraped = source.get("last_scraped")
        interval = source.get("interval_hours", 24)

        if should_scrape(last_scraped, interval):
            print(f"\n🌐 Scraping : {name} ({url})")
            try:
                html = fetch_page_content(url)
                print("✅ Page récupérée.")

                summary = summarize_content(html)
                print(f"📄 Résumé extrait :\n{summary[:300]}...")

                store_vector(url, summary)
                print("✅ Contenu stocké.")

                source["last_scraped"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                updated = True

            except Exception as e:
                print(f"❌ Erreur pendant le scraping de {name} : {e}")

    if updated:
        save_schedule(schedule)
        print("\n📂 Planning mis à jour avec les nouvelles dates de scraping.")
    else:
        print("\n⏳ Rien à scraper pour le moment.")


if __name__ == "__main__":
    auto_scrape()
