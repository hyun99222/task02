#!/usr/bin/python3
from scapy.all import *

TTl=0


a = IP()
b = ICMP()
a.dst = "8.8.8.8"
 a.ttl = TTL+1
 p = a/b
 send(p)

