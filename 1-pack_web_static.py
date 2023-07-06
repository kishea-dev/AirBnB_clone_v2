#!/usr/bin/python3
'''Fabric script to generate .tgz archive'''

from fabric.api import local
from datetime import datetime
from fabric.decorators import runs_once
from os.path import isdir


@runs_once
def do_pack():
    '''generates .tgz archive from the contents of the web_static folder'''
    try:
        date = datetime.now().strftime("%Y%m%d%H%M%S")
        if isdir("versions") is False:
            local("mkdir versions")
        file_name = "versions/web_static_{}.tgz".format(date)
        local("tar -cvzf {} web_static".format(file_name))
        return file_name
    except:
        return None
