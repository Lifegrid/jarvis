import os
from datetime import datetime
from core.llm_interface import generate_code_from_prompt

PATCHES_DIR = "patches"

os.makedirs(PATCHES_DIR, exist_ok=True)

def generate_and_test_patch() -> str:
    """
    Jarvis tente de générer un patch pour s'améliorer et le sauvegarde dans un fichier.
    """
    try:
        prompt = (
            "Analyse ton propre code en tant qu'IA et propose une amélioration simple, claire et utile.\n"
            "Génère uniquement le contenu du fichier corrigé sans explication autour.\n"
            "Format : commence directement par le code (Python)."
        )

        patch_code = generate_code_from_prompt(prompt)

        if "def" not in patch_code and "class" not in patch_code:
            return "❌ La génération ne semble pas contenir de vrai code. Patch ignoré."

        timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
        patch_filename = f"patch_{timestamp}.py"
        patch_path = os.path.join(PATCHES_DIR, patch_filename)

        with open(patch_path, "w", encoding="utf-8") as f:
            f.write(patch_code)

        return f"✅ Patch généré et sauvegardé dans {patch_filename}."
    
    except Exception as e:
        return f"❌ Erreur lors de la génération de patch : {str(e)}"
