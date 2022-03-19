import subprocess
from sys import argv
from os import path

def check_venv():
    if path.isdir("./venv"):
        pass
    else:
        subprocess.Popen(["python3", "-m", "venv", "venv"])

def main():
    check_venv()
    sub = argv[0]
    if sub == "install":
        subprocess.Popen(["venv/bin/pip", "install", argv[1]])
        print("インストール完了！")
