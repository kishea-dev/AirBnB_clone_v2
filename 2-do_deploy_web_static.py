#!/usr/bin/python3
"""
AirBnB clone - Deploy static, task 2. Deploy archive!
"""
from datetime import datetime
from fabric.api import *
import shlex
import os

env.hosts = ['54.83.128.139', '34.207.64.39']
env.user = 'ubuntu'


def do_deploy(archive_path):
    """ Distributes a .tgz archive from the contents of `web_static/` in AirBnB
    clone repo to the web servers
    Retruns:
        (bool): `True` if all operations successful, `False` otherwise
    """
    if exists(archive_path) is False:
        return False
    try:
        file_n = archive_path.split("/")[-1]
        no_ext = file_n.split(".")[0]
        path = "/data/web_static/releases/"
        put(archive_path, '/tmp/')
        run('mkdir -p {}{}/'.format(path, no_ext))
        run('tar -xzf /tmp/{} -C {}{}/'.format(file_n, path, no_ext))
        run('rm /tmp/{}'.format(file_n))
        run('mv {0}{1}/web_static/* {0}{1}/'.format(path, no_ext))
        run('rm -rf {}{}/web_static'.format(path, no_ext))
        run('rm -rf /data/web_static/current')
        run('ln -s {}{}/ /data/web_static/current'.format(path, no_ext))
        return True
    except:
        return False
