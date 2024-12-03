#!/usr/local/bin/python3
#==========
# 21.py
#==========

'''
one report per line
each report - list of numbers (levels) separated by spaces
safe report:
    all levels are either all increasing or all decreasing
    any two adjacent levels differ by at least one and at most 3

452 is too high
'''

import sys


matrix = []

for line in sys.stdin:

    rpt = []

    line = line.rstrip()    # remove any white space from end of string

    flds = line.split()

    for x in flds:
        rpt.append(int(x))

    matrix.append(rpt)


num_safe = 0


for rrow in matrix:

    j = -1

    safe = False

    print ("\norig_row=",rrow)

    while True:

        safe = True

        row = rrow.copy()

        if j >= 0:
            if j < len(row):
                row.pop(j)
                print ("rm - ",j , " row=", row)
            else:
                print ("hit end of loop")
                safe = False
                break

        j += 1

        ascending = False
        descending = False

        for i in range (1,len(row)):
            if row[i-1] < row[i]:
                ascending = True
            elif row[i-1] > row[i]:
                descending = True
            else:   
                # equal
                safe = False
                print ("not safe - equal")
                break
    
            if ascending and descending:
                safe = False
                print ("not safe - a/d")
                break
    
            diff = abs(row[i-1] - row[i])
    
            if diff < 1 or diff > 3:
                safe = False
                print ("not safe - diff out of range")
                break

        if safe:
            break

    if safe:
        print ("safe")
        num_safe += 1
    
print (num_safe)
