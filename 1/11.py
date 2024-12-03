#!/usr/local/bin/python3
#==========
# 
#==========

import sys


l1 = []
l2 = []

for line in sys.stdin:

    line = line.rstrip()    # remove any white space from end of string

    flds = line.split()

    if len(flds) != 2:
        raise ("Invalid Line")

    l1.append(int(flds[0]))
    l2.append(int(flds[1]))

if len(l1) != len(l2):
    raise ("Invalid Lists")


l1.sort()
l2.sort()

diff = 0

for x in range(len(l1)):

    diff += abs (l1[x]-l2[x])

print (diff)
