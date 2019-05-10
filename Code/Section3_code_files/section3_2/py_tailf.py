# credit: http://code.activestate.com/recipes/157035-tail-f-in-python/

import time, os

#Set the filename and open the file
filename = 'nexus.log'
file = open(filename,'r')

#Find the size of the file and move to the end
st_results = os.stat(filename)
st_size = st_results[6]
file.seek(st_size)

while 1:
    where = file.tell()
    line = file.readline()
    if not line:
        time.sleep(1)
        file.seek(where)
    else:
        print(line) # already has newline

