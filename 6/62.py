#!/usr/local/bin/python3
#==========
# 62.py
#==========

import sys

UP = 1
DOWN = 2
LEFT = 3
RIGHT = 4

width = 0
height = 0

matrix = []

def move (pos):

    visited = set()

    visited.add(pos)
    
    x = pos[0]
    y = pos[1]
    direction = pos[2]

    while True:

        sav_x = x
        sav_y = y
        sav_direction = direction

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
            return False
    
        if y < 0 or y > height-1:
            return False


        if matrix[y][x] != '#':

            # not an obstacle

            print ("visited -",x,y)

            if (x,y,direction) in visited:
                # infinite loop
                print ("x=",x,"y=",y,"direction=", direction,"already present - infinite loop")
                return True

            visited.add((x,y,direction))
            continue

        # if here, avoid obstacle

        if direction == UP:
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


direction = UP

count = 0

for y in range (height):
    for x in range (width):
        if matrix[y][x] != '#':
            print ("x=",x,"y=",y,"...")
            sav_str  = matrix[y]
            temp_str = matrix[y][:x] + '#' + matrix[y][x+1:]
            matrix[y] = temp_str
            pos = (start[0], start[1], direction)
            rc = move (pos)
            matrix[y] = sav_str
            if rc:
                print ("x=",x,"y=",y,"infinite loop!")
                count += 1

print ("count=",count)
   

