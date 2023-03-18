# 스티커
# DP

#input 
""" 
2
5
50 10 100 20 40
30 50 70 10 60
7
10 30 10 50 100 20 40
20 40 30 50 60 20 80
""" 

import sys

num = int(input())

for i in range(num):
    x = int(input())
    li = []

    for k in range(2):
        li.append(list(map(int, input().split())))

    for j in range(1, x):
        if j == 1 :
            li[0][j] += li[1][j - 1]
            li[1][j] += li[0][j - 1]
        else:
            li[0][j] += max(li[1][j - 1], li[1][j - 2])
            li[1][j] += max(li[0][j - 1], li[0][j - 2])

    
    print(max(li[0][x - 1], li[1][x - 1]))
    # print(li)