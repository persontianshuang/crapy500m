from fabric.api import *
from fabric.contrib.console import confirm


env.hosts = [
    'root@45.76.135.68',
    'root@45.76.140.76',
    'root@45.76.134.241',
]

env.passwords = {
    'root@45.76.135.68:22': 'v_Q9hHg48.XMp9hj',
    'root@45.76.140.76:22': '2rZ$xW4v%ahd4Hf_',
    'root@45.76.134.241': '8P?dpT@=w+5-Z@NU',
}


def echo():
    run("apt-get update")
    run("export LC_ALL=C")
    run("apt install python3-pip -y")
    run("apt install git")
    run("pip3 install pymongo redis requests lxml gevent")
    run("git clone https://github.com/persontianshuang/crapy500m.git")
    run("ls")
