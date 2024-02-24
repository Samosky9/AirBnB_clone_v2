#!/usr/bin/python3

""" Packs the web_static to a tar """

from fabric.api import local
from datetime import datetime


def do_pack():
    """ A function to pack the current webstatic version """

    local('mkdir -p versions')

    current = datetime.now()
    filename = "versions/web_static_{}{}{}{}{}{}.tgz".format(
        current.year, current.month, current.day,
        current.hour, current.minute, current.second)

    path = local('tar -cvzf {} web_static'.format(filename))
    if path.succeeded:
        print("Packed webstatic to {}".format(filename))
        return filename
    else:
        return None
