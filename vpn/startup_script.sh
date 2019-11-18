#!/bin/bash
/bin/bash /root/tun.sh
sleep 5
/bin/bash /root/config_iptables.sh
sleep 5
echo nameserver 1.1.1.1 > /etc/resolv.conf 
openvpn /etc/openvpn/VPN001/*.ovpn > /tmp/openvpn.out
#while true; do echo 'Hit CTRL+C'; sleep 1; done