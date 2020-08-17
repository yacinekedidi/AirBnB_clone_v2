#!/usr/bin/python3
"""Module"""
from fabric.api import *
import os

env.user = 'ubuntu'
env.hosts = ['35.190.159.176', '35.229.61.48']


def do_clean(number=0):
    """function"""
    n = 1 if int(number) == 0 else int(number)

    a = sorted(os.listdir("versions"))
    for i in range(n):
        a.pop()
    with lcd("versions"):
        [local("rm -rf {}".format(x)) for x in a]
    with cd("/data/web_static/releases"):
        l = run("ls -tr").split()
        for i in range(n):
            l.pop()
        [run("rm -rf {}".format(x)) for x in l]
