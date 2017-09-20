from fabric.api import *
from fabric.contrib.console import confirm


env.hosts = ['my_server']

def hello():
    print("Hello world!")



def deploy():
    code_dir = '/Users/user/work/py/crapy500m/fabric'
    with cd(code_dir):
        run("ls")

