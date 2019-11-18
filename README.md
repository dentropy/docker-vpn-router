# docker-vpn-router

Example of createing a VPN gateway within a docker network using docker-compose

## Prerequisites

* Computer with docker compose and Python3
* A VPN to connect to or a [Private Internet Access](https://www.privateinternetaccess.com/) account

## Setup

* Using [Private Internet Access](https://www.privateinternetaccess.com/)
  * Add pass.txt in the following format in the ovpn folder

    ``` bash
    username
    password
    ```

  * run the python script labled addpassword.py within that directory

    ``` bash
    cd ./vpn/ovpn
    python3 addpassword.py
    ```

* Uring your own VPN('s)
  * Create folder VPN### inside ovpn folder where the ### are a number
  * Put the desired ovpn file in VPN### folder
  * If password is required know that the location of VPN### is at /etc/openvpn/VPN###

## Deploying

* Use a terminal to navigate to this directory

``` bash
sudo docker-compose up
```

## Testing it works

``` bash
# get the status of the VPN
docker exec -ti dockervpnrouter_vpn_1 cat /tmp/openvpn.out

# get the IP of the container
docker exec -ti dockervpnrouter_client_1 curl ifconfig.co

# test both gateways
docker exec -ti dockervpnrouter_client_1 route del default
docker exec -ti dockervpnrouter_client_1 route add default gw 172.78.0.1
docker exec -ti dockervpnrouter_client_1 curl ifconfig.co
docker exec -ti dockervpnrouter_client_1 route del default
docker exec -ti dockervpnrouter_client_1 route add default gw 172.78.0.123
docker exec -ti dockervpnrouter_client_1 curl ifconfig.co
```
