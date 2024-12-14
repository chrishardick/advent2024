#!/usr/local/bin/python3
#==========
# 101.py
#==========

import sys
import re


#
# main
# 

pattern = '0'

matrix = []
trailheads = []

y = 0

for line in sys.stdin:

    line = line.rstrip()

    res = re.finditer(pattern,line)

    if res:
        for match in res:
            x = match.start()
            trailheads.append((x,y))

    matrix.append(line)

    y += 1


print ("matrix")
for line in matrix:
    print (line)

print ("")
print ("trailheads")
for pt in trailheads:
    print (pt)


    

