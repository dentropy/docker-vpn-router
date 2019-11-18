#!/bin/bash
mkdir -p /dev/net
mknod /dev/net/tun c 10 200
chmod 600 /dev/net/tun
#cat /dev/net/tun