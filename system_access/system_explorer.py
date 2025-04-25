import os

def list_files(directory="."):
    try:
        entries = os.listdir(directory)
        return [entry for entry in entries]
    except Exception as e:
        return [f"Erreur lors de l'exploration : {str(e)}"]

def get_absolute_path(filename):
    return os.path.abspath(filename)

def file_exists(path):
    return os.path.exists(path)

if __name__ == "__main__":
    print("📁 Contenu du dossier courant :")
    print(list_files())
