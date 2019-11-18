#!/bin/bash
docker network create \
  --driver=bridge \
  --subnet=172.78.0.0/16 \
  vpn_test_network
docker run -d --name my_vpn --dns=1.1.1.1 --network="vpn_test_network" --ip="172.78.0.123" --cap-add=NET_ADMIN vpn_router
docker run -it --name vpn_test --dns=1.1.1.1 --network="vpn_test_network" --ip="172.78.0.8" --cap-add=NET_ADMIN ubuntu:updated
#sleep 3
#docker exec -it vpn_test bash