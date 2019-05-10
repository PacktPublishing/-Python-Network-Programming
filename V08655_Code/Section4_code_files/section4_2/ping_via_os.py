#!/usr/bin/env python3

import os

host_list = ['www.cisco.com', 'www.google.com', '192.168.2.1']

for host in host_list: 
    os.system('ping -c 1 ' + host)


