import pandas as pd
import os

def analyze_csv(path: str) -> str:
    """Analyse intelligente d’un fichier CSV"""
    if not os.path.exists(path):
        return "[Erreur] Fichier introuvable."

    try:
        df = pd.read_csv(path)

        info = {
            "colonnes": list(df.columns),
            "taille": f"{len(df)} lignes × {len(df.columns)} colonnes",
            "manquants": df.isnull().sum().to_dict(),
            "types": df.dtypes.astype(str).to_dict()
        }

        stats = df.describe(include='all').to_string()

        résumé = (
            f"# Analyse du fichier CSV : {os.path.basename(path)}\n\n"
            f"**Dimensions** : {info['taille']}\n"
            f"**Colonnes** : {', '.join(info['colonnes'])}\n\n"
            f"## Types de données\n{info['types']}\n\n"
            f"## Valeurs manquantes\n{info['manquants']}\n\n"
            f"## Statistiques principales :\n```\n{stats}\n```"
        )

        return résumé

    except Exception as e:
        return f"[Erreur analyse CSV] {str(e)}"

# Test CLI
if __name__ == "__main__":
    output = analyze_csv("data/raw/exemple.csv")
    print(output[:1500])
