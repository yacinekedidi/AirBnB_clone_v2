#!/usr/bin/python3
"""Module"""
from fabric.api import put, env, run
from datetime import datetime
import os.path

env.user = 'ubuntu'
env.hosts = ['35.190.159.176', '35.229.61.48']


def do_deploy(archive_path):
    """function"""
    if not os.path.exists(archive_path):
        return False
    put(archive_path, "/tmp")
    f = archive_path.split("/")[-1]
    name = f.split('.')[0]
    new_dir = "{}{}".format("/data/web_static/releases/", name)

    run("mkdir -p {}".format(new_dir))

    run("tar xzf /tmp/{} -C {}".format(f, new_dir))

    run("rm -rf /tmp/{}".format(f))

    run("mv {}/web_static/* {}".format(new_dir, new_dir))

    run("rm -rf {}/web_static".format(new_dir))

    run("rm -rf {}".format("/data/web_static/current"))

    run("ln -s {} {}".format(new_dir, "/data/web_static/current"))

    return True
