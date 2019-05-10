#!/usr/env/bin python3

import subnet_calculator_v1

network = '192.168.1.0/29'

cal = subnet_calculator_v1.subnet_calculator(network)
print(cal.network)


