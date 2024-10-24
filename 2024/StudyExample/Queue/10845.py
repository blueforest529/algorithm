"""
15
push 1
push 2
front
back
size  
empty
pop
pop
pop
size
empty
pop
push 3
empty
push 1

12312321
"""

import sys
sys.setrecursionlimit(10000)

arr = []
ll = []
N = int(input())

for i in range(N):
    ll.append(input())

for k in ll:   
    j = k.split()

    if j[0] == 'push':
        arr.append(j[1])

    if j[0] == 'pop':
        if len(arr) > 0 :
            print(arr.pop(0))
        else :
            print(-1)

    if j[0] == 'front':
        if len(arr) > 0 :
            print(arr[0])
        else :
            print(-1)

    if j[0] == 'back':
        if len(arr) > 0 :
            print(arr[-1])
        else :
            print(-1)

    if j[0] == 'size':
        print(len(arr))

    if j[0] == 'empty':
        if len(arr) > 0 :
            print(0)
        else :
            print(1)

