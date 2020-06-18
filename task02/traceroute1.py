#!/usr/bin/python3
from scapy.all import *

TTL=0
while(True):
	TTL += 1
	a = IP(dst="1.2.3.4",ttl=TTL)
        
	b = ICMP()
	p = a/b
       
	reply = sr(p)
	print("IP: ", reply[IP].src)
	if (reply[IP].src == "1.2.3.4"):
	
