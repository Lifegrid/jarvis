def decide_action(message: str, profile: dict) -> str:
    if "trop de travail" in message:
        return "Propose une pause ou une tâche plus légère."
    if "motivation" in message:
        return "Joue un message motivant ou propose un petit objectif."
    if profile.get("mode") == "focus":
        return "Filtrer distractions et rappeler l'objectif principal."
    return "Analyse simple, aucun plan spécial déclenché."

