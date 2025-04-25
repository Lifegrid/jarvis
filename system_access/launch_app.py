import subprocess
import platform

def open_chrome():
    if platform.system() == "Windows":
        subprocess.Popen("start chrome", shell=True)
    else:
        subprocess.Popen(["google-chrome"])

def open_vscode():
    subprocess.Popen("code", shell=True)

def open_terminal():
    if platform.system() == "Windows":
        subprocess.Popen("start cmd", shell=True)
    else:
        subprocess.Popen(["gnome-terminal"])
