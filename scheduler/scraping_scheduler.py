import json
import time
from datetime import datetime, timedelta
import os
from web_scraper.web_navigator import fetch_page_content
from web_scraper.content_summarizer import summarize_content
from web_scraper.source_vectorizer import store_vector

CONFIG_PATH = "config/scraping_sources.json"
SCHEDULE_PATH = "config/scraping_schedule.json"
LAST_RUN_PATH = "config/last_scrape.json"


def load_json(path):
    if os.path.exists(path):
        with open(path, 'r', encoding='utf-8') as f:
            return json.load(f)
    return {}


def save_json(path, data):
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4)


def should_scrape(last_time_str, interval_hours):
    if not last_time_str:
        return True
    last_time = datetime.fromisoformat(last_time_str)
    return datetime.now() - last_time > timedelta(hours=interval_hours)


def scrape_all_sources():
    sources = load_json(CONFIG_PATH)
    schedule = load_json(SCHEDULE_PATH)
    last_run = load_json(LAST_RUN_PATH)
    interval_hours = schedule.get("interval_hours", 24)

    for source in sources:
        name = source["name"]
        url = source["url"]

        if not should_scrape(last_run.get(name), interval_hours):
            print(f"⏭️ Déjà scrapé récemment : {name}")
            continue

        print(f"\n🌐 Scraping de : {name} ({url})")
        try:
            html = fetch_page_content(url)
            print("✅ Page récupérée.")
            content = summarize_content(html)
            print(f"📄 Résumé : {content[:100]}...")
            store_vector(url, content)
            print("💾 Stocké dans la mémoire vectorielle.")
            last_run[name] = datetime.now().isoformat()
        except Exception as e:
            print(f"❌ Erreur pour {name} : {e}")

    save_json(LAST_RUN_PATH, last_run)


if __name__ == "__main__":
    while True:
        print("\n🔁 Vérification du scraping planifié...")
        scrape_all_sources()
        sleep_time = load_json(SCHEDULE_PATH).get("check_every_minutes", 60)
        print(f"⏳ Prochaine vérification dans {sleep_time} minutes...")
        time.sleep(sleep_time * 60)
