import os

def write_code_to_file(code, filename="auto_code.py", folder="generated_code"):
    if not os.path.exists(folder):
        os.makedirs(folder)
    path = os.path.join(folder, filename)
    with open(path, "w", encoding="utf-8") as f:
        f.write(code)
    return path
