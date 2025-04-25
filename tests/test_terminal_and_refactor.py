# tests/test_terminal_and_refactor.py

from code_executor.code_writer import save_code
from code_executor.code_executor import run_python_code
from code_executor.terminal_adapter import run_command
from code_executor.code_refactor import refactor_code

# 1. Créer du code
code = """
print("   Hello   depuis JARVIS ")
x =  10
print("Résultat :", x + 32  )
"""

# 2. Refactoriser
refactored = refactor_code(code)
print("\n🔁 Code refactorisé :\n", refactored)

# 3. Sauvegarder dans un fichier
file_path = save_code(refactored, filename="refactor_test")

# 4. Lancer ce code directement avec Python
result = run_python_code(refactored)
print("\n⚙️ Exécution Python :")
print("STDOUT:", result["stdout"])
print("STDERR:", result["stderr"])

# 5. Ou exécuter une commande système (Windows uniquement ici)
cmd_result = run_command("echo Hello depuis PowerShell")
print("\n💻 Commande système :")
print("STDOUT:", cmd_result["stdout"])
print("STDERR:", cmd_result["stderr"])
