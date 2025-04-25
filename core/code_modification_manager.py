from autonomous_code_modification import read_file, generate_patch, compare_versions, backup_file, restore_backup
from git_manager import create_branch, commit_changes, push_changes
import os

def apply_patch(file_path: str, patch_details: str):
    """
    Applique un patch à un fichier source.
    """
    try:
        # Sauvegarde du fichier avant modification
        backup_path = backup_file(file_path)

        # Lire le contenu actuel du fichier
        content = read_file(file_path)

        # Générer le patch basé sur le contenu et les détails fournis
        patched_file_path = generate_patch(file_path, content, patch_details)

        # Comparer les versions avant et après patch
        original_content = content
        modified_content = read_file(patched_file_path)
        diff_output = compare_versions(original_content, modified_content)
        print("Diff entre les versions :\n", diff_output)

        # Commiter les changements dans Git
        create_branch("dev")
        commit_changes(f"Applied patch: {patch_details}")
        push_changes()

        print(f"Patch appliqué avec succès. Le fichier est sauvegardé à : {patched_file_path}")
    except Exception as e:
        print(f"Erreur lors de l'application du patch : {e}")
        restore_backup(file_path, backup_path)

# Exemple d'utilisation
apply_patch("main.py", "Ajout de la gestion des erreurs pour améliorer la résilience.")
