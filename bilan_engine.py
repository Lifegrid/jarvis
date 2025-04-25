import datetime
from web_memory import get_recent_web_memories


def generate_daily_bilan() -> str:
    """
    Génère un bilan intelligent à partir des mémoires web récentes.
    """
    memories = get_recent_web_memories(hours=24)
    if not memories:
        return "📅 Aucun souvenir marquant enregistré aujourd'hui."

    lignes = ["\n\ud83d\udcca **Bilan intelligent du jour :**"]
    for item in memories:
        date = item.get("timestamp", "(date inconnue)")
        title = item.get("title", "(sans titre)")
        summary = item.get("summary", "(aucun résumé)")
        lignes.append(f"\n\ud83d\udd39 **{title}**\n{summary}\n")

    return "\n".join(lignes)


def should_run_bilan() -> bool:
    """
    Vérifie si le bilan doit être exécuté (1 fois par jour).
    """
    try:
        with open(".last_bilan.txt", "r") as f:
            last_date = f.read().strip()
        if last_date == datetime.date.today().isoformat():
            return False
    except FileNotFoundError:
        pass

    with open(".last_bilan.txt", "w") as f:
        f.write(datetime.date.today().isoformat())
    return True