# tests/test_code_executor.py

from code_executor.code_executor import run_python_code

code = """
# -*- coding: utf-8 -*-
print("Hello Jérém")
x = 42
print("Résultat :", x * 2)
"""

result = run_python_code(code)

print("✅ Résultat de l'exécution :")
print("STDOUT:", result["stdout"])
print("STDERR:", result["stderr"])
print("Code retour:", result["returncode"])
