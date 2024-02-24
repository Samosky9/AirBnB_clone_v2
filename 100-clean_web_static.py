#!/usr/bin/python3

"""deletes out-of-date archives from the versions folder """

from fabric.api import run, runs_once, local, put, env
from datetime import datetime
import os


env.user = 'ubuntu'
env.hosts = ['18.234.106.179', '34.207.83.122']


@runs_once
def do_pack():
    """ A function to pack the current webstatic version """

    current = datetime.now()
    filename = "versions/web_static_{}{}{}{}{}{}.tgz".format(
        current.year, current.month, current.day,
        current.hour, current.minute, current.second)

    local('mkdir -p versions')
    path = local('tar -cvzf {} web_static'.format(filename))
    if path.succeeded:
        print("Packed webstatic to {}".format(filename))
        return filename
    else:
        return None


def do_deploy(archive_path):
    """ Deploys a webstatic to a webserver """

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
    print("New version deployed!")

    return True


def deploy():
    """ PACk and deploy """

    version = do_pack()
    if not version:
        return False

    return do_deploy(version)


@runs_once
def clean_machine(number):
    """ Cleans trhe machine of archives """

    version_list = local('ls versions', capture=True).split('\n')
    store = 1 if number == 0 else number
    remov = version_list[: -store]
    if len(remov) == 0:
        return

    for i in range(len(remov)):
        remov[i] = "versions/{}".format(remov[i])

    remov = " ".join(remov)
    local('rm -rf {}'.format(remov))


def clean_remote(number):
    """ Cleans the remote srver """

    versions = run("ls /data/web_static/releases | grep web_static")
    versions = versions.stdout.split("\n")

    store = 1 if number == 0 else number
    remov = versions[: -store]
    if len(remov) == 0:
        return

    for i in range(len(remov)):
        remov[i] = "/data/web_static/releases/{}".format(remov[i])

    remov = " ".join(remov)
    run('sudo rm -rf {}'.format(remov))


def do_clean(number=0):
    """ Cleaner for web_static archives """

    number = int(number)
    clean_machine(number)
    clean_remote(number)
