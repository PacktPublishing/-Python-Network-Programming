#! /usr/bin/env python3

import sys
from scapy3k.all import sr1,IP,ICMP

p=sr1(IP(dst=sys.argv[1])/ICMP())
if p:
    p.show()


