#!/usr/bin/python3
"""fabric script to generate a .tgz archive from web_static"""
from fabric.api import *
from datetime import datetime
from os



env.hosts = ['35.237.127.124', '34.74.215.227']


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

def do_deploy(archive_path):
    """ distributes an archive to web serers, using do_deply """
    if not os.path.isfile(archive_path) is 0:
        return False
    try:
        put(archive_path, "/tmp/")
        a_path = archive_path[9:-4]
        run("sudo mkdir -p /data/web_static/releases/web_static_{}/".format(a_path))
        run("sudo tar -xzf /tmp/web_static_{}.tgz -C "
            "/data/web_static/releases/web_static_{}".format(a_path, a_path))
        run("sudo rm /tmp/web_static_{}.tgz".format(a_path))
        run("sudo mv -f /data/web_static/releases/web_static_{}/web_static/* "
            "/data/web_static/releases/web_static_{}/".format(a_path, a_path))
        run("sudo rm -rf /data/web_static/releases/"
            "web_static{}/web_static".format(a_path))
        run("sudo rm -rf /data/web_static/current")
        run("sudo ln -s /data/web_static/releases/"
            "web_static_{}/ /data/web_static/current".format(a_path))
    except:
        return False
    else:
        return True
