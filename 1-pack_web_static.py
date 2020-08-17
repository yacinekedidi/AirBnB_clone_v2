#!/usr/bin/python3
"""Module"""
from fabric.api import local
from datetime import datetime
import os.path


def do_pack():
    """function"""
    dt = datetime.now()
    arch_name = "versions/web_static_{}.tg\
    z".format(dt.strftime("%Y%m%d%H%M%S"))
    if not os.path.exists("versions/"):
        os.mkdir("versions")
    local("tar -cvzf {} web_static".format(arch_name))
    if os.path.exists("{}".format(arch_name)):
        return arch_name
    else:
        return None
