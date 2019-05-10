#!/usr/bin/env python3

import subprocess

host_list = ['www.cisco.com', 'www.google.com', '192.168.2.1']

for host in host_list:
    print('*' * 10)
    print('host: ' + host)
    p = subprocess.Popen(['ping', '-c', '1', host], stdout=subprocess.PIPE)
    print(p.communicate())

