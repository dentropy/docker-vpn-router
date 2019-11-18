FROM ubuntu:18.04

RUN apt update -y
RUN apt install -y openvpn 
RUN apt install -y net-tools
RUN apt install -y iptables 
RUN apt install -y iputils-ping
RUN apt install -y nano
RUN apt install -y curl
RUN apt install -y wget
COPY startup.sh /root/startup.sh
CMD ["/bin/bash", "/root/startup.sh"]