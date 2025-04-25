import zipfile
import os

def explore_zip_file(path: str) -> str:
    """Liste le contenu d’un fichier ZIP"""
    if not os.path.exists(path):
        return "[Erreur] Fichier introuvable."

    if not zipfile.is_zipfile(path):
        return "[Erreur] Le fichier fourni n’est pas une archive ZIP valide."

    try:
        with zipfile.ZipFile(path, 'r') as archive:
            file_list = archive.infolist()
            if not file_list:
                return "[Info] L’archive est vide."

            result = f"# Contenu de l’archive : {os.path.basename(path)}\n\n"
            for file in file_list:
                result += f"- {file.filename} ({file.file_size} octets)\n"
            return result

    except Exception as e:
        return f"[Erreur lecture ZIP] {str(e)}"

# Test CLI
if __name__ == "__main__":
    contenu = explore_zip_file("data/raw/exemple.zip")
    print(contenu)
