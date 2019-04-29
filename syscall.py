#!/usr/bin/env python

import subprocess

def uname_fun():
    uname = "uname"
    uname_arg = "-a"
    subprocess.call([uname,uname_arg])

def disk_fun():
    diskspace = "df"
    diskspace_arg = "-h"
    subprocess.call([diskspace, diskspace_arg])

def main():
    uname_fun()
    disk_fun()

main()
