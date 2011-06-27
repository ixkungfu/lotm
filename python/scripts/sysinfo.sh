#!/bin/bash
# A System Information Gathering Script
# sysinfo.sh

#command 1
uname_func()
{
    UNAME="uname -a"
    printf "Gathering system infomation with the $UNAME command: \n\n"
    $UNAME
}

#command 2
disk_func()
{
    DISKSPACE="df -h"
    printf "Gathering diskspace information with the $DISKSPACE command: \n\n"
    $DISKSPACE
}

main()
{
    uname_func
    disk_func
}

main
