import os
from system_access.file_explorer import explore_and_store


def test_exploration():
    base_path = "docs"
    if not os.path.exists(base_path):
        os.makedirs(base_path)
        with open(os.path.join(base_path, "exemple.txt"), "w", encoding="utf-8") as f:
            f.write("Ce document teste l'importation et le résumé automatique d'un fichier texte dans Jarvis.")

    explore_and_store(base_path)


if __name__ == "__main__":
    test_exploration()
