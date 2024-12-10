#!/usr/local/bin/python3
#==========
# 81.py
#==========

import sys
import re

from collections import defaultdict

matrix = []

# points[key] = [pt1,pt2,...ptN)
points = defaultdict(list)

# for each pt combination
# pt[key] = [ (pt1, pt2, m, b), ...]
pt = defaultdict(list)

pattern = r"[a-zA-Z0-9]"

line_num = 0

for line in sys.stdin:

    line = line.rstrip()

    matrix.append(line)

    res = re.finditer(pattern,line)

    for match in res:

        idx = match.start()

        char = line[idx]

        points[char].append((idx, line_num))

    line_num += 1

print (points)


for char in points:

    lst = points[char]

    for i in lst:
        for j in lst:
            if i != j:
                m = (i[1]-j[1])/(i[0]-j[0])
                b = i[1]-m*i[0]
                pt[(char)].append((i,j,m,b))

print (pt)
print ()

matches = defaultdict(list)

for char in sorted(pt):

    print ("key=|",char,"|...")

    for y in range(len(matrix)):
        for x in range(len(matrix[0])):
            if matrix[y][x] == char:
                continue
            for i in pt[char]:
                m = i[2]
                b = i[3]

                if y == m*x + b:
                    # point is on the same line

                    p1 = i[0]
                    p2 = i[1]

                    dist_p1 = abs(p1[0]-x)+abs(p1[1]-y)
                    dist_p2 = abs(p2[0]-x)+abs(p2[1]-y)

                    if (dist_p1 == 2*dist_p2 or 
                        dist_p2 == 2*dist_p1):

                        print ("(", x ,",", y, ") is a match")
                        matches[(x,y)].append("")

print (matches)
print ("count=",len(matches))
