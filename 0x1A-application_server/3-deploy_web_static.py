#!/usr/bin/python3
"""This module fully deploys the web_static folder"""
import os
from fabric.api import *
from datetime import datetime


env.hosts = ['35.231.108.101', '35.185.107.146']
env.user = 'ubuntu'


def do_pack(current_pack=[]):
    """Pack the web_static into a .tgz file"""
    if not current_pack == []:
        return current_pack[0]

    if not os.path.exists('versions'):
        local('mkdir versions')
    cmd = 'tar -cvzf versions/web_static_'
    time = datetime.now()
    time = time.strftime("%Y%m%d%H%M%S")
    cmd = cmd + time + '.tgz web_static'
    res = local(cmd)

    if res.failed:
        return None
    current_pack.append('versions/web_static_' + time + '.tgz')
    return current_pack[0]


def do_deploy(archive_path):
    """deploy a .tgz file to the servers"""
    fname = archive_path.split("/")[-1]
    short = fname.split(".")[0]
    good = True

    path_test = local("test -e " + archive_path)
    if path_test.failed:
        return False

    x = put(archive_path, '/tmp/' + fname)

    y = run('mkdir -p /data/web_static/releases/' + short + '/')

    temp = 'tar -xzf /tmp/' + fname
    temp = temp + ' -C /data/web_static/releases/' + short + '/'
    z = run(temp)

    a = run('rm /tmp/' + fname)

    temp = 'mv /data/web_static/releases/' + short + '/web_static/*'
    temp = temp + ' /data/web_static/releases/' + short + '/'
    b = run(temp)

    temp = 'rm -rf /data/web_static/releases/' + short + '/web_static'
    c = run(temp)

    d = run('rm -rf /data/web_static/current')

    temp = 'ln -s /data/web_static/releases/' + short + '/'
    temp = temp + ' /data/web_static/current'
    e = run(temp)

    good = good and x.succeeded
    good = good and y.succeeded
    good = good and z.succeeded
    good = good and a.succeeded
    good = good and b.succeeded
    good = good and c.succeeded
    good = good and d.succeeded
    good = good and e.succeeded

    return good


def deploy():
    path = do_pack()
    if path is None:
        return False

    return do_deploy(path)
