# -*- coding: utf-8 -*-

from glustercli.cli.utils import gluster_execute

def glusterfs_version():
    """Return the GlusterFS version"""
    cmd = ["--version"]
    # The library takes care of raising exception in case of any errors
    version_line = gluster_execute(cmd).split('\n')[0]

    return version_line.split(' ')[1]