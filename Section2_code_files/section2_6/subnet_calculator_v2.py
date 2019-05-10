#!/usr/bin/env python3
import ipaddress

class subnet_calculator:
    def __init__(self, network):
        self.network = network
        self.net = ipaddress.IPv4Network(network)

    # Test if an IP is in the subnet
    def ip_in_subnet(self, ip):
        if ipaddress.IPv4Address(ip) in list(self.net.hosts()):
            return True
        else:
            return False
    
    # Is my network part of another network
    def my_net_to_another(self, network):
        if self.net.overlaps(ipaddress.IPv4Network(network)):
            return True
        else:
            return False

    # DNS PTR Record from IP
    # note the staticmethod without self in method
    @staticmethod
    def ip_to_ptr(ip):
        return ipaddress.ip_address(ip).reverse_pointer
   

if __name__ == "__main__":
    net1 = subnet_calculator('192.168.1.0/24')
    print(net1.network)


