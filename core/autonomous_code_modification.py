import os
import difflib
import shutil

def read_file(file_path: str) -> str:
    """
    Cette fonction lit un fichier et retourne son contenu sous forme de chaîne.
    """
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Le fichier {file_path} n'existe pas.")
    
    with open(file_path, 'r') as file:
        return file.read()


def generate_patch(file_path: str, content: str, patch_details: str) -> str:
    """
    Cette fonction génère un patch pour un fichier donné et l'enregistre.
    """
    # Simuler la modification en ajoutant un commentaire avec le patch proposé
    patch = f"# PATCH: {patch_details}\n{content}\n"
    
    # Enregistrer le patch dans un nouveau fichier
    patched_file_path = file_path.replace(".py", "_patched.py")
    
    with open(patched_file_path, 'w') as file:
        file.write(patch)
    
    return patched_file_path


def compare_versions(original: str, modified: str) -> str:
    """
    Cette fonction compare deux versions de fichiers et génère un diff.
    """
    diff = difflib.unified_diff(
        original.splitlines(),
        modified.splitlines(),
        fromfile='original.py',
        tofile='modified.py',
    )
    return '\n'.join(diff)


def backup_file(file_path: str) -> str:
    """
    Effectue une sauvegarde du fichier avant toute modification.
    """
    backup_path = f"{file_path}.backup"
    shutil.copy(file_path, backup_path)
    return backup_path


def restore_backup(file_path: str, backup_path: str):
    """
    Restaure un fichier à partir de sa sauvegarde.
    """
    shutil.copy(backup_path, file_path)
    print(f"Restauration du fichier {file_path} à partir de {backup_path}")
