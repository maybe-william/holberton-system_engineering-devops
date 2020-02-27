#!/usr/bin/python3
"""This module fully deploys the web_static folder cleanly"""
import re
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
    """Do the full deployment"""
    path = do_pack()
    if path is None:
        return False

    return do_deploy(path)


def do_clean(number=0):
    """Clean excess deployments down to the most recent number"""
    num = int(number)
    if num < 0:
        return
    if num == 0:
        num = 1

    def get_deletable(listing, number):
        """Get the items to delete"""
        patt = re.compile('web_static_\d{14}')
        lines = str(listing).split("\n")

        lines = list(filter(patt.search, lines))

        lines = sorted([x.split(' ')[-1].rstrip() for x in lines])
        lines.reverse()
        print("sorted")
        print(lines)
        if len(lines) > number:
            return lines[number:len(lines)]
        return []

    with lcd('versions'):
        loc = local("ls -l .", capture=True)
        locd = get_deletable(loc.stdout, num)
        for i in locd:
            local("rm " + i)

    with cd('/data/web_static/releases'):
        rem = run("ls -l .")
        remd = get_deletable(rem.stdout, num)
        for i in remd:
            run("rm -r " + i)
