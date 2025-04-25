import shutil
import os

def backup_file(file_path: str) -> str:
    """
    Effectue une sauvegarde du fichier avant toute modification.
    """
    backup_path = f"{file_path}.backup"
    shutil.copy(file_path, backup_path)
    print(f"Sauvegarde effectuée dans : {backup_path}")
    return backup_path


def restore_backup(file_path: str, backup_path: str):
    """
    Restaure un fichier à partir de sa sauvegarde.
    """
    shutil.copy(backup_path, file_path)
    print(f"Restauration du fichier {file_path} à partir de {backup_path}")
