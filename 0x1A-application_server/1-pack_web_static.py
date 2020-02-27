#!/usr/bin/python3
"""This module compresses the web_static folder"""
import os
from fabric.api import *
from datetime import datetime


def do_pack():
    """Pack the web_static into a .tgz file"""
    if not os.path.exists('versions'):
        local('mkdir versions')
    cmd = 'tar -cvzf versions/web_static_'
    time = datetime.now()
    time = time.strftime("%Y%m%d%H%M%S")
    cmd = cmd + time + '.tgz web_static'
    res = local(cmd)
    if res.failed:
        return None
    return 'versions/web_static_' + time + '.tgz'
