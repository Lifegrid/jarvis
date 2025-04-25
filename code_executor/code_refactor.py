# code_executor/code_refactor.py

def refactor_code(code: str) -> str:
    """
    Applique une transformation simple : nettoyage des espaces inutiles,
    mise en forme des indentations, normalisation des retours à la ligne.
    """
    lines = code.strip().splitlines()
    cleaned_lines = [line.rstrip() for line in lines if line.strip() != '']
    return '\n'.join(cleaned_lines)
