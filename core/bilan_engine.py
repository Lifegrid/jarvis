from datetime import datetime
from core.memory_engine import search_memory
import pytz

def generate_daily_bilan(date: str = None, timezone: str = "Europe/Paris") -> str:
    """Génère un bilan de la journée à partir des souvenirs en mémoire vectorielle"""
    if not date:
        now = datetime.now(pytz.timezone(timezone))
        date = now.strftime("%Y-%m-%d")

    # Cherche les souvenirs liés à cette date
    keywords = [date, "aujourd'hui", "bilan", "résumé", "journal", "réflexion"]
    results = []
    for k in keywords:
        results.extend(search_memory(k, n_results=5))

    if not results:
        return "Aucun souvenir pertinent trouvé pour aujourd'hui."

    texte_bilan = f"**Bilan Jarvis pour le {date}**\n\n"
    for doc, meta in results:
        source = meta.get("source", "inconnu")
        cat = meta.get("category", "général")
        texte_bilan += f"→ *{cat}* ({source}) : {doc.strip()[:250]}...\n\n"

    return texte_bilan.strip()
