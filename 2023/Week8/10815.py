# 숫자 카드
"""
5
6 3 2 10 -10
8
10 9 -5 2 3 4 5 -10
"""

N1 = int(input())
C1 = list(map(int,input().split()))
N2 = int(input())
C2 = list(map(int,input().split()))

_dict = {}  
for i in range(N1):
    _dict[C1[i]] = 0 

for j in range(N2):
    if C2[j] in _dict:
        print(1, end='')
    else :
        print(0, end='')
    print(' ', end='')

