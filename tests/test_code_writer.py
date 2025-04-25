# tests/test_code_writer.py

from code_executor.code_writer import save_code

code = """
# -*- coding: utf-8 -*-
print("Hello depuis le fichier écrit par JARVIS 🧠")
"""

path = save_code(code, file_type="py", filename="hello_jarvis")

print(f"✅ Fichier créé ici : {path}")
