FROM ubuntu:18.04

RUN apt update -y
RUN apt install -y openvpn net-tools iptables 
RUN apt install -y iputils-ping
RUN apt install -y nano
RUN apt install -y curl
RUN apt install -y wget
RUN apt install -y lynx
COPY startup.sh /root/startup.sh
CMD ["/bin/bash", "/root/startup.sh"]