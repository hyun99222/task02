#!/usr/bin/python3
from scapy.all import *



def print_pkt(pkt):                       
   print("Source IP:", pkt[IP].src)
   print("Destination IP:", pkt[IP].dst)
   print("Protocol:", pkt[IP].proto)
   

pkt = sniff(filter='icmp',prn=print_pkt)   
