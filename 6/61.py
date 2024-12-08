#!/usr/local/bin/python3
#==========
# 61.py
#==========

import sys

UP = 1
DOWN = 2
LEFT = 3
RIGHT = 4

width = 0
height = 0

matrix = []

visited = set()

def move (pos, direction):

    visited.add(pos)
    
    x = pos[0]
    y = pos[1]

    while True:

        sav_x = x
        sav_y = y

        if direction == UP:
            y -= 1
    
        elif direction == DOWN:
            y += 1
    
        elif direction == LEFT:
            x -= 1
    
        elif direction == RIGHT:
            x += 1
    
        else:
            raise "INVALID DIRECTION"
    
    
        if x < 0 or x > width-1:
            return len(visited)
    
        if y < 0 or y > height-1:
            return len(visited)


        if matrix[y][x] != '#':
            print ("visited -",x,y)
            visited.add((x,y))
            continue

        elif direction == UP:
            direction = RIGHT
        elif direction == DOWN:
            direction = LEFT
        elif direction == LEFT:
            direction = UP
        elif direction == RIGHT:
            direction = DOWN

        x = sav_x
        y = sav_y


start = None

for line in sys.stdin:

    line = line.rstrip()

    for x in range(len(line)):
        if line[x] == '^':
            start = (x, len(matrix))

    matrix.append(line)


print ("start=", start)

width = len(matrix[0])
height = len(matrix)

print ("width=",width)
print ("height=",height)


pos = start
direction = UP

print ("#pos=",move (pos, direction))


   

