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
    sub = argv[1]
    if sub == "install":
        subprocess.Popen(["venv/bin/pip", "install", argv[1:]], stdout=subprocess.PIPE)
        print("インストール完了！")
