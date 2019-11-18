#!/bin/bash
route add default gw 172.78.0.123
while true; do echo 'Hit CTRL+C'; sleep 1; done