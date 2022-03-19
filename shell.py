import subprocess
from sys import argv
from os import path

def check_venv():
    if path.isdir("./venv"):
        pass
    else:
        subprocess.run(["python3", "-m", "venv", "venv"])

def main():
    sub = argv[0]
    if sub == "install":
        pass
