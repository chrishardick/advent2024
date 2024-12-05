#!/usr/local/bin/python3
#==========
# 42.py
#
# 2028 is too high
#==========

import sys

matrix = []

num_matches = 0


def search (x, y):

    global matrix
    global xmas 
    global num_matches

    # print ("search: idx=",idx, "(", x, ",", y, ")")

    deltas =    [   (-1,-1), ( 1,-1),
                    (-1, 1), ( 1, 1)
                ]

    match = True

    p = []

    for d in range(len(deltas)):
        x1 = x + deltas[d][0]
        y1 = y + deltas[d][1]

        if x1 < 0 or x1 >= len(matrix[0]):
            # invalid x
            print ("invalid x", x1)
            match = False
            break

        if y1 < 0 or y1 >= len(matrix):
            # invalid y
            print ("invalid y", y1)
            match = False
            break

        p.append(matrix[y1][x1])

    if not match:
        return

    if p[0] == "M" and p[1] == "S" and p[2] == "M" and p[3] == "S":
        num_matches += 1
    elif p[0] == "S" and p[1] == "M" and p[2] == "S" and p[3] == "M":
        num_matches += 1

    elif p[0] == "M" and p[1] == "M" and p[2] == "S" and p[3] == "S":
        num_matches += 1
    elif p[0] == "S" and p[1] == "S" and p[2] == "M" and p[3] == "M":
        num_matches += 1


#    p.sort()
#
#    if p[0] == "M" and p[1] == "M" and p[2] == "S" and p[3] == "S":
#        num_matches += 1

#    return

#    if (((p[0] == "M" and p[1] == "S") or (p[0] == "S" and p[1] == "M")) and
#       ((p[2] == "M" and p[3] == "S") or (p[2] == "S" and p[3] == "M"))):
#
#        num_matches += 1
#        print ("match!")
#
#    else:
#        print ("not a match", p)
#        
#    return

#
# main
#

for line in sys.stdin:

    line = line.rstrip()        # remove any white space from end of string

    matrix.append(line)



for y in range(len(matrix)):

    for x in range(len(matrix[y])):

        if matrix[y][x] == 'A':

            print ("\nmain: x=", x, "y=", y)

            search(x,y)


print ("num_match=",num_matches)
