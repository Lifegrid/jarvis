def generate_insight(messages: list[dict], context: str = "") -> str:
    """Analyse le contexte pour suggérer une réflexion ou une idée."""
    recent = messages[-1]["content"] if messages else ""
    if "crypto" in recent.lower():
        return "🔎 Il serait pertinent de surveiller les tendances du marché crypto aujourd'hui."
    elif "fatigue" in recent.lower():
        return "🛌 Tu sembles fatigué, tu devrais peut-être ajuster ta routine du soir."
    return "🤔 Rien à signaler pour l'instant, mais je reste en alerte."