# autonomous_cycle.py

from web_memory import store_web_memory, get_web_memory
from web_research import autonomous_web_research
from memory_engine.memory_utils import store_memory_snapshot
from datetime import datetime


def autonomous_cycle(message: str, profile: dict) -> None:
    """
    Fonction principale de boucle intelligente :
    - détecte des opportunités d'apprentissage
    - mémorise des éléments utiles
    - enrichit la mémoire web
    - prépare un résumé pour futur usage
    """
    if not message:
        return

    if any(w in message.lower() for w in ["cours", "derniers résultats", "actualité", "prix"]):
        result = autonomous_web_research(message)
        store_web_memory(query=message, summary=result)
        store_memory_snapshot(content=result, category="web_research")

    if "bilan" in message.lower():
        generate_daily_summary()


def generate_daily_summary():
    """
    Génère un petit rapport/bilan autonome de la journée (à afficher ou sauvegarder).
    """
    memories = get_web_memory()
    date = datetime.now().strftime("%d/%m/%Y")
    lines = [f"# Bilan du {date}\n"]
    if not memories:
        lines.append("Aucune recherche web sauvegardée aujourd'hui.")
    else:
        for mem in memories[-3:]:  # Les 3 plus récentes
            lines.append(f"- {mem['timestamp']} | {mem['query']}\n  {mem['summary'][:300]}...")

    bilan = "\n".join(lines)
    store_memory_snapshot(content=bilan, category="daily_summary")
    print(bilan)  # Peut être retourné ou envoyé dans l'UI aussi
