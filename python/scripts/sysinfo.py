#!/usr/bin/env python
# A System Information Gathering Script
# sysinfo.py
import subprocess

#command 1
def uname_func():
    uname = "uname"
    uname_arg = "-a"
    print "Gathering system information with %s command:\n" % uname
    subprocess.call([uname, uname_arg])

#command 2
def disk_func():
    disk = "df"
    disk_arg = "-h"
    print "Gathering diskspace information %s command:\n" % disk
    subprocess.call([disk, disk_arg])

#Main function
def main():
    uname_func()
    disk_func()

if __name__ == "__main__":
    main()
