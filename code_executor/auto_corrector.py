import traceback

def analyze_and_fix_code(code: str):
    """
    Simule une analyse du code et retourne une version corrigée s'il détecte des erreurs simples.
    (En production, cette fonction pourrait être connectée à un modèle LLM local ou une analyse syntaxique plus poussée.)
    """
    try:
        # Essayons d'exécuter le code en sandbox pour détecter les erreurs
        exec(code, {}, {})
        return code, None  # Le code est valide
    except Exception as e:
        # Si une erreur est détectée, on la capture et on propose une correction simple
        error = traceback.format_exc()
        corrected_code = _attempt_correction(code, error)
        return corrected_code, error

def _attempt_correction(code: str, error: str):
    """
    Méthode naïve pour corriger certaines erreurs simples (exemple : print manquant des parenthèses)
    """
    if "SyntaxError" in error and "print" in code and "print " in code:
        # Correction print sans parenthèses (ex : Python 2 vers Python 3)
        return code.replace("print ", "print(").replace("\n", ")\n")
    elif "NameError" in error:
        # Tentative de remplacement de variables non définies par 0
        lines = code.split("\n")
        fixed_lines = []
        for line in lines:
            if "NameError" in error and "=" in line:
                fixed_lines.append(line)
            elif line.strip():
                fixed_lines.append("# Erreur détectée ici : " + line)
            else:
                fixed_lines.append(line)
        return "\n".join(fixed_lines)
    else:
        # Si pas de correction possible automatique
        return code + "\n# [Aucune correction automatique disponible]"
