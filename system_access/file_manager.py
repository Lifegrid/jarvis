import os
import shutil

def create_file(name="test_jarvis.txt", content=""):
    path = os.path.join(os.getcwd(), name)
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
    return path

def delete_file(name):
    path = os.path.join(os.getcwd(), name)
    if os.path.exists(path):
        os.remove(path)
        return True
    return False

def move_file(source_name, destination_path):
    source_path = os.path.join(os.getcwd(), source_name)
    if os.path.exists(source_path):
        shutil.move(source_path, destination_path)
        return True
    return False
