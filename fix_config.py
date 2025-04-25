import json
import os

config = [
    {
        "name": "CoinMarketCap",
        "category": "crypto",
        "url": "https://coinmarketcap.com/",
        "frequency": "daily"
    },
    {
        "name": "Journal du Coin",
        "category": "crypto",
        "url": "https://journalducoin.com/",
        "frequency": "daily"
    }
]

os.makedirs("config", exist_ok=True)

with open("config/scraping_schedule.json", "w", encoding="utf-8") as f:
    json.dump(config, f, indent=4, ensure_ascii=False)

print("✅ Fichier scraping_schedule.json régénéré avec succès.")
