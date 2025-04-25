def suggest_next_actions(context: str) -> list[str]:
    if "crypto" in context:
        return ["🧮 Compare les prix sur CoinGecko", "📈 Lance une veille sur les altcoins"]
    if "sommeil" in context:
        return ["💤 Proposer une routine de sommeil", "🕒 Ajuster les heures de réveil"]
    return ["🤖 Proposer de nouvelles tâches", "🧠 Résumer les derniers faits appris"]