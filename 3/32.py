#!/usr/local/bin/python3
#==========
# 32.py
#==========

import sys
import re

regex = r'do\(\)|don\'t\(\)|mul\(([0-9]{1,3}),([0-9]{1,3})\)'

res = 0

print ("ON (start value)")
on = True

for line in sys.stdin:

    line = line.rstrip()    # remove trailing white space

    match = re.finditer (regex, line)

    for m in match:

        if m.group() == "do()":
            print ("ON")
            on = True
        elif m.group() == "don't()":
            print ("OFF")
            on = False
        else:
            if on:
                print (m.group(1), m.group(2))

                i = int(m.group(1))
                j = int(m.group(2))

                res += i*j
        
print (res)
