#!/usr/bin/env python3

import time, timeit, requests

start = time.time()
t = timeit.Timer('requests.get("http://www.google.com")', "import requests")
times_p1 = t.repeat(5, 1)
stop = time.time()

print(stop - start)
print(times_p1)

