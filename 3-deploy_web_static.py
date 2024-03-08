#!/usr/bin/python3

""" packs and deploys a new version to the server """


import os
from fabric.api import env, local, run, put, runs_once
from datetime import datetime

env.user = 'ubuntu'
env.hosts = ['52.91.118.128', '54.197.89.146']


@runs_once
def do_pack():
    """ A function to pack the current webstatic version to an archive """

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


def do_deploy(archive_path):
    """ Deploys a webstatic to a webserver through thescript crreated and """

    if not os.path.isfile(archive_path):
        return False

    packname = archive_path.split("versions/")[-1]
    temppath = "/tmp/{}".format(packname)
    comppath = "/data/web_static/releases/{}/".format(packname[:-4])

    put(archive_path, temppath)
    run('mkdir -p {}'.format(comppath))
    comp = run('tar -xzf {} -C {}'.format(temppath, comppath))
    if comp.failed:
        return False
    run('rm {}'.format(temppath))
    run('mv {}/web_static/* {}'.format(comppath, comppath))
    run('rm -rf {}/web_static/'.format(comppath))
    run('rm -rf /data/web_static/current')
    run('ln -sf {} /data/web_static/current'.format(comppath))
    print("Uploaded {} to servers".format(archive_path))

    return True


def deploy():
    """
        Pack and deploy function for task 3, creates an archive, then sends
        it to a server
    """

    version = do_pack()
    if not version:
        return False

    return do_deploy(version)
