#!/usr/local/bin/python3
#==========
# 41.py
#==========
'''
..X...
.SAMX.
.A..A.
XMAS.S
.X....

    x-1,y-1     x,y-1   x+1,y-1
    x-1,y       x,y     x+1,y
    x-1,y+1     x,y+1   x+1,y+1
'''

import sys

xmas="XMAS"

matrix = []

num_matches = 0


def search (idx, x, y, dx, dy):

    global matrix
    global xmas 
    global num_matches

    # print ("search: idx=",idx, "(", x, ",", y, ")")

    if idx == len(xmas):
        num_matches += 1
        return
   
    if x < 0 or x >= len(matrix[0]):
        # invalid x
        return

    if y < 0 or y >= len(matrix):
        # invalid y
        return

    if matrix[y][x] == xmas[idx]:
        print ("x=", x
                ," y=", y
                ," got a"
                , xmas[idx])

        search (idx+1, x+dx, y+dy, dx, dy)

#
# main
#

for line in sys.stdin:

    line = line.rstrip()        # remove any white space from end of string

    matrix.append(line)



deltas = [  (-1,-1) , (0,-1), (1,-1),
            (-1,0)  , (1,0) ,
            (-1,1)  , (0,1) , (1,1)]

for y in range(len(matrix)):

    for x in range(len(matrix[y])):

        if matrix[y][x] == xmas[0]:

            print ("main: x=", x, "y=", y)

            for d in deltas:
                search (0,x,y,d[0],d[1])
            
                '''print ("main: x=", x
                        ," y=", y 
                        ," dx=", d[0]
                        ," dy=", d[1])'''




print ("num_match=",num_matches)
