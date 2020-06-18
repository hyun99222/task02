#!/usr/bin/python3
from scapy.all import *

a = IP()
a.dst = "10.0.2.6"
a.src="10.0.2.45"
b = ICMP()
p = a/b
p.show()
send(p)

