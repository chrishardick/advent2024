#!/usr/local/bin/python3
#==========
# 51.py
#==========

import sys

from collections import defaultdict

rules=True


# for entry e, all the values which must come before
# after -> before set
after = defaultdict(set)

# all entries which must come after
# before -> after set
before  = defaultdict(set)

updates = []

for line in sys.stdin:

    line = line.rstrip()

    if len(line) == 0:
        rules=False
        continue

    if rules:

        # before|after
        flds = line.split('|')
        
        b = flds[0]
        a = flds[1]

        after[a].add(b)

        continue

    else:

        # update sets

        flds = line.split(',')

        updates.append(flds)


print ("after=",after,"\n")
print ("before=",before,"\n")
print ("updates=",updates,"\n")

line_num = 0

total = 0

for line in updates:

    ok = True

    line_num += 1

    print ("line ",line_num,":", line, "...")

    for i in range(len(line)):

        # these are the values coming after
        # - we need to make sure they're not supposed to come before
        print (line[i], "ascending...")
        for a in range(i+1,len(line)):
            print (line[a])
            if line[a] in after[line[i]]:
                ok = False
                break
        print ("")

        if not ok:
            continue

        print (line[i], "descending...")
        for d in range(i-1,-1,-1):
            print (line[d])
            if line[d] in before[line[i]]:
                ok = False
                break

        print ("")

    if ok:
        total += int(line[int(len(line)/2)])
        print ("GOOD LINE:", line, "TOTAL=",total)

    print ("")

print ("total=",total)
