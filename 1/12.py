#!/usr/local/bin/python3
#==========
# 12.py
#
# how often each number from the left list appears in the right
# add up each number in the left list after multiplying it by hte number of times it appears in the right
#
# create a dictionary
# traverse right hand list, load dictionary 
# traverse left handl list, look up right hand...
#==========

'''
3   4
4   3
2   5
1   3
3   9
3   3
'''

import sys


l1 = []

d = {}

for line in sys.stdin:

    line = line.rstrip()    # remove any white space from end of string

    flds = line.split()

    if len(flds) != 2:
        raise ("Invalid Line")

    l1.append(int(flds[0]))

    rhs = int(flds[1])

    if rhs in d:
        d[rhs] += 1
    else:
        d[rhs] = 1


sum = 0

for x in l1:

    if x in d:
        sum += x*d[x]

print (sum)
