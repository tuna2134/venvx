import subprocess
from sys import argv
import venv
from os import path

def check_venv():
    if path.isdir("./venv"):
        pass
    else:
        venv.create("venv", clean=True, with_pip=True)

def main():
    check_venv()
    sub = argv[1]
    
    if sub == "install":
        subprocess.run(["./venv/bin/pip", "install"] + argv[2:], stdout=subprocess.PIPE)
        print("実行完了！")
        
    elif sub == "uninstall":
        p = subprocess.Popen(["./venv/bin/pip", "uninstall"] + argv[2:], stdin=subprocess.PIPE, stdout=subprocess.PIPE)
        p.stdin.write(b'y')
        p.stdin.close()
        p.wait()
        print("実行完了！")
        
    elif sub == "list":
        subprocess.run(["./venv/bin/pip", "list"] + argv[2:])
