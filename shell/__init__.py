import subprocess
from sys import argv
from os import path

def check_venv():
    if path.isdir("./venv"):
        print(True)
    else:
        subprocess.Popen(["python3", "-m", "venv", "venv"])
        print(False)

def main():
    check_venv()
    sub = argv[0]
    if sub == "install":
        subprocess.Popen(["venv/bin/pip", "install", argv[1]])
        print("インストール完了！")
