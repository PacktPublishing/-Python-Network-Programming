#!/usr/bin/env python3

import pyspeedtest

test = pyspeedtest.SpeedTest()
print("Your Ping Time")
print(str(test.ping()) + "ms")

print("Your Download Speed")
print(str(test.download()) + "bps")

print("Your Upload Speed")
print(str(test.upload()) + "bps")

