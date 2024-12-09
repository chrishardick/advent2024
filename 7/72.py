#!/usr/local/bin/python3
#==========
# 72.py
#
# 850 lines
# looks like about 10 operators per line
# 3^9 for each line
#==========

import sys

def ternary (n):
    if n == 0:
        return '0'

    nums = ""
    while n:
        n, r = divmod(n,3)
        nums += str(r)

    return str(nums[::-1])


res = []
operands = []

lines = []

for line in sys.stdin:

    line = line.rstrip()

    lines.append(line)

    l1 = line.split(':')

    if len(l1) != 2:
        raise ("invalid line -", line)

    res.append(int(l1[0]))

    l2 = l1[1].split()

    for i in range(len(l2)):
        l2[i] = int(l2[i])
        
    operands.append(l2)
    

total = 0


# for each line

line_num = 0

for i in range(len(res)):

    lcl_operands = operands[i]

    num_operands = len(lcl_operands)
    num_operators = num_operands-1

    print ("\nline # ", line_num, " ",lines[i])
    line_num += 1

    #print ("operands=", lcl_operands)
    #print ("#operands=",num_operands)
    #print ("#operators=",num_operators)

    num_combo = 3**(num_operators)       # #possible combinations

    print ("#combo=",num_combo)

    for j in range(num_combo):    # for each operator combination
    
        # construct operator combination

        tnum = ternary(j)   # convert to ternary
        tnum = tnum.zfill(num_operators)

        #print ("j=", j, "ternary=",tnum)

        operators = []

        for pos in range(num_operators):     # 0,1,...

            #print ("pos=",pos)

            if tnum[pos] == '0':
                operators.append('*')
            elif tnum[pos] == '1':
                operators.append('+')
            elif tnum[pos] == '2':
                operators.append('||')
            else:
                raise ("invalid ternary number - ", tnum)

        #print ("operators=",operators)

        lcl_result = 0

        for k in range(len(operators)):

            #print ("k=",k)

            if k == 0:
                if operators[k]=='*':
                    lcl_result = lcl_operands[k]*lcl_operands[k+1]
                elif operators[k]=='+':
                    lcl_result = lcl_operands[k]+lcl_operands[k+1]
                else:
                    lcl_result = int (str(lcl_operands[k]) + str(lcl_operands[k+1])) 

            else:
                if operators[k]=='*':
                    lcl_result *= lcl_operands[k+1]
                elif operators[k]=='+':
                    lcl_result += lcl_operands[k+1]
                else:
                    lcl_result = int( (str(lcl_result)+str(lcl_operands[k+1])) )

        if lcl_result == res[i]:
            # valid line
            print ("valid line!")
            total += res[i]
            break
               

print ("total=",total)
