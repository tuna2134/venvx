import subprocess
from sys import argv
from os import path

def check_venv():
    if path.isdir("./venv"):
        pass
    else:
        subprocess.run(["python3", "-m", "venv", "venv"], stdout=subprocess.PIPE)

def main():
    check_venv()
    sub = argv[1]
    if sub == "install":
        subprocess.run(["venv/bin/pip", "install"] + argv[1:], stdout=subprocess.PIPE)
        print("実行完了！")
    elif sub == "uninstall":
        subprocess.run(["venv/bin/pip", "uninstall"] + argv[1:], input="y", stdout=subprocess.PIPE)
        print("実行完了！")
