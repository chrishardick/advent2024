#!/usr/local/bin/python3
#==========
# 72.py
#==========

import sys

def ternary (n):
    if n == 0:
        return '0'

    nums = []
    while n:
        n, r = divmod(n,3)
        nums.append(str(r))

    return nums[::-1]


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

for i in range(len(res)):

    lcl_operands = operands[i]

    num_operands = len(lcl_operands)
    num_operators = num_operands-1

    print ("line=",lines[i],"num_operands=",num_operands,"#operators",num_operators)

    num_combo = 3**(num_operators)       # #possible combinations

    print ("#combo=",num_combo)

    for j in range(num_combo):    # for each operator combination
    
        # construct operator combination

        tnum = ternary(j)

        operators = []

        for pos in range(num_operators):     # 0,1,...

            if tnum[pos] == '0':
                operators.append('*')
            elif tnum[pos] == '1':
                operators.append('+')
            elif tnum[pos] == '2':
                operators.append('||')
            else:
                raise ("invalid ternary number - ", tnum)

        print ("operators=",operators)

        lcl_result = 0

        for k in range(len(operators)):

            print ("k=",k)

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
            total += res[i]
            break
               

print ("total=",total)
