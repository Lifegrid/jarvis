import subprocess

def create_branch(branch_name: str):
    """
    Crée une nouvelle branche Git.
    """
    subprocess.run(['git', 'checkout', '-b', branch_name])
    print(f"Branche {branch_name} créée et activée.")


def commit_changes(commit_message: str):
    """
    Effectue un commit avec un message spécifique.
    """
    subprocess.run(['git', 'add', '.'])
    subprocess.run(['git', 'commit', '-m', commit_message])
    print(f"Changements commités avec le message : {commit_message}")


def push_changes():
    """
    Pousse les changements sur le dépôt distant.
    """
    subprocess.run(['git', 'push'])
    print("Changements poussés sur le dépôt distant.")


def checkout_branch(branch_name: str):
    """
    Change de branche Git.
    """
    subprocess.run(['git', 'checkout', branch_name])
    print(f"Passé à la branche {branch_name}.")
