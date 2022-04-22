from os import path
import subprocess
from venv import EnvBuilder

projects_dir = path.join(path.abspath(path.dirname(__name__)), 'projects')

class PipEnv:
    def __init__(self, name, libs):
        self.env = EnvBuilder(clear=True, with_pip=True)
        if not path.isdir(f"{projects_dir}/{name}"):
            self.env.create(f"{projects_dir}/{name}")
        self.pip = f"{projects_dir}/{name}/bin/pip"
        
    def do_pip(self, cmd: list, **kwargs):
        subprocess.run([self.pip] + cmd,
                       stdout=subprocess.PIPE,
                       stderr=subprocess.STDOUT,
                       **kwargs)
            
    def install(self, name, *args):
        self.do_pip(["install", name] + list(args))
        print("Complete")
        
    def uninstall(self, name, *args):
        self.do_pip(["uninstall", name, "-y"] + list(args))
        print("Complete")
