FROM ubuntu:18.04

RUN apt update -y
RUN apt install -y openvpn 
RUN apt install -y net-tools
RUN apt install -y iptables 
RUN apt install -y iputils-ping
RUN apt install -y nano
RUN apt install -y curl
RUN apt install -y wget
COPY ovpn /etc/openvpn/
COPY config_iptables.sh /root/config_iptables.sh
COPY startup_script.sh /root/startup_script.sh
COPY tun.sh /root/tun.sh
CMD ["/bin/bash", "/root/startup_script.sh"]