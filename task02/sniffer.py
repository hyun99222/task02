#!/usr/bin/python3


from scapy.all import *

def print_pkt(pkt):
   pkt.show()

#pkt = sniff(filter='icmp',prn=print_pkt) 
pkt = sniff(filter='tcp port 23, prn=print_pkt)
#pkt = sniff(filter='net 126.18.0.0/16, prn=print_pkt)



