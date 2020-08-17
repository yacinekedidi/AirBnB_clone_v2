#!/usr/bin/python3
"""Module"""
from fabric.api import local
from datetime import datetime
import os.path


def do_pack():
    """function"""
    dt = datetime.now()
    an = "versions/web_static_{}.tgz".format(dt.strftime("%Y%m%d%H%M%S"))
    if not os.path.exists("versions/"):
        os.mkdir("versions")
    local("tar -cvzf {} web_static".format(an))
    if os.path.exists("{}".format(an)):
        return an
    else:
        return None
