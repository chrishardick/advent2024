#!/usr/local/bin/python3
#==========
# 31.py
#==========

import sys
import re

regex = r'mul\(([0-9]{1,3}),([0-9]{1,3})\)'

res = 0

for line in sys.stdin:

    line = line.rstrip()    # remove trailing white space

    match = re.finditer (regex, line)

    for m in match:
        print (m.group(1), m.group(2))

        i = int(m.group(1))
        j = int(m.group(2))

        res += i*j
        
print (res)
