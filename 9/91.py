#!/usr/local/bin/python3
#==========
# 91.py
#==========

import sys
import re

from collections import defaultdict

#==========
# 12345 => 0..111....22222
# file 0 for 1
# 2 blank spaces
# file 1 for 3
# 4 blank spaces
# file 2 for 5
#==========
def expand_line (line):

    out = []

    Id = 0

    for idx in range(len(line)):

        if (idx % 2) == 0:
            # even - file

            for i in range(int(line[idx])):
                out.append(str(Id))

            Id += 1

        else:
            # odd - free space
           
            for i in range(int(line[idx])):
                out.append(".")

    return out

# trim trailing space 
def trim_trailing_space (line): # in/out

    for idx in range(len(line)-1, -1, -1):
        if line[idx] == ".":
            line.pop(idx)
        else:
            break

def get_last_size (line, left_idx):

    trim_trailing_space(line)

    # at this point, last entry should not be empty

    # start from end, search for file entry (not .)
    # should be 1st entry
    # else return None

    print ("get_last_size: length of line =", len(line)-1, "left_idx=",left_idx)

    for idx in range (len(line)-1, left_idx, -1):

        print ("get_last_size: idx=",idx)

        if line[idx] != ".":
            char = line[idx]
            line.pop(idx)
            print ("get_last_size: returning", char)
            return int(char)
        else:
            print ("line[idx]=",line[idx])

    trim_trailing_space(line)
    print ("get_last_size: returning None")
    return None


# 0..111....22222 => 022111222
# size=15            size=9

def move_items (line):
   
    line_len = len(line)

    idx = 0

    while idx < line_len:

        if line[idx] == ".":

            print ("got . at", idx)

            # starts at end of string and returns last file id
            ret = get_last_size(line,idx)

            if not ret:
                return

            print ("replacing idx", idx, "with", ret)
            line[idx] = ret

            line_len = len(line)

        idx += 1


def calc_checksum (lst):

    res = 0

    for i in range(len(lst)):

        if lst[i] != '.':
            res += i * int(lst[i])
  
    return res

#
# main
# 

for line in sys.stdin:

    line = line.rstrip()

ll = []
for l in line:
    ll.append(l)
    
print ("line=", ll, "\n")

eline = expand_line(ll)
print ("eline=",eline, "\n")

print ("trimming trailing space...")
trim_trailing_space (eline)
print ("eline=",eline, "\n")

print ("moving items...")
move_items (eline)
print ("eline=",eline, "\n")

print ("")
chksum = calc_checksum (eline)
print ("chksum=", chksum)

