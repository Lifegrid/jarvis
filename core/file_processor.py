def summarize_file(filename: str, contents: bytes) -> str:
    """
    Produit un résumé simple pour un fichier uploadé.
    """
    try:
        text = contents.decode('utf-8', errors='ignore')
        lines = text.splitlines()
        preview = "\n".join(lines[:10])  # Résumé simple = 10 premières lignes

        return f"📄 Fichier: {filename}\n\nRésumé rapide:\n{preview}"
    except Exception as e:
        return f"❌ Erreur lors du traitement du fichier : {str(e)}"
