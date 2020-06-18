#!/usr/bin/python3
from scapy.all import *

def print_pkt(pkt):
    a = IP()
    b = ICMP()
    a.dst = '10.0.2.6'
    send(a / b)

pkt=sniff(filter='icmp and host 10.0.2.6', prn=print_pkt)

