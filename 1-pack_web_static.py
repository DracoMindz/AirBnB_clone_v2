#!/usr/bin/python3
"""fabric script to generate a .tgz archive from web_static"""
from fabric.api import *
from datetime import datetime


def do_pack():
    """
    Stores contents of web_static in compressed archive.
    Return the archive path if the archive has been correctly generated.
    Otherwise, it should return None

    """
    local('mkdir -p versions')
    time = datetime.now().strftime("%Y%m%d%H%M%S")
    result = local('tar -czvf versions/web_static_{}.tgz web_static'
                   .format(time))
    if result.failed:
        return None
    else:
        return result
