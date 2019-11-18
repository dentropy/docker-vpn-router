FROM ubuntu:18.04

RUN apt update -y
RUN apt install -y openvpn net-tools iptables 
RUN apt install -y iputils-ping
RUN apt install -y nano
# dnsutils iptables-persistent
COPY ovpn /etc/openvpn/
COPY config_iptables.sh /root/config_iptables.sh
COPY startup_script.sh /root/startup_script.sh
COPY tun.sh /root/tun.sh
#RUN bash /root/tun.sh
#RUN bash /root/config_iptables.sh
CMD ["/bin/bash", "/root/startup_script.sh"]
#CMD ["/bin/bash", "-c", "while true; do sleep 1000; done"]
#CMD ["openvpn /etc/openvpn/001/*.ovpn"]