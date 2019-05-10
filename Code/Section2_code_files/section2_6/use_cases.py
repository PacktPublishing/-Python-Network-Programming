#!/usr/env/bin python3

import subnet_calculator_v2

ip = '192.168.1.1'
network = '192.168.1.4/30'

cal = subnet_calculator_v2.subnet_calculator('192.168.1.0/29')

print("My network is {0}".format(cal.network))
print("Is ip {0} in my network?".format(ip))
print(cal.ip_in_subnet('192.168.1.1'))
print("Is network {0} a subnet in my network?".format(ip))
print(cal.my_net_to_another('192.168.1.4/30'))

print("The PTR record for ip {0} is:".format(ip))
# note how the method is called without an instance of the object
print(subnet_calculator_v2.subnet_calculator.ip_to_ptr(ip))


