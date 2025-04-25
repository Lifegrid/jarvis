def analyze_uploaded_file(filepath: str) -> str:
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()
        return f"📎 Analyse de fichier :\n\n{content[:1000]}\n\n(Résumé automatique à venir…)"
    except Exception as e:
        return f"⚠️ Erreur lors de la lecture du fichier : {e}"
