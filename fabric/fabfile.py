from fabric.api import *
from fabric.contrib.console import confirm




def hello():
    print("Hello world!")


def deploy():
    code_dir = '/Users/user/work/py/crapy500m/fabric'
    with cd(code_dir):
        local("ls")

env.hosts = [
    'root@188.166.148.251',
]

env.passwords = {
    'root@188.166.148.251:22': '',
}


def echo():
    run("ls")
