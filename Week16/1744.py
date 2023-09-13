
"""
4
-1
2
1
3
"""

import sys
input = sys.stdin.readline
N = int(input())
plus = []
minus = []
newArr = []

for i in range(N):
    number = int(input())
    if number <= 0 :
        minus.append(number)

    if number > 0 :
        plus.append(number)


if len(minus) == 1:
    newArr.append(minus[0])
else :
    minus.sort()
    
    for i in range(0, len(minus), 2):
        if i >= len(minus)-1 :
            newArr.append(minus[i])
        else :
            newArr.append(minus[i] * minus[i+1])
        

if len(plus) == 1:
    newArr.append(plus[0])
else :
    plus.sort(reverse=True)
    
    for i in range(0, len(plus), 2) :
        if i >= len(plus)-1 :
            newArr.append(plus[i])
        else :
            mix = plus[i] * plus[i+1]
            if mix <= plus[i] :
                newArr.append(plus[i])    
                newArr.append(plus[i+1])    
            else :
                newArr.append(plus[i] * plus[i+1])
            
print(sum(newArr))
