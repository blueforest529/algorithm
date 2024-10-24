#로또

"""
7 1 2 3 4 5 6 7
8 1 2 3 5 8 13 21 34
0

1 2 3 4 5 6
1 2 3 4 5 7
1 2 3 4 6 7
1 2 3 5 6 7
1 2 4 5 6 7
1 3 4 5 6 7
2 3 4 5 6 7
"""
import sys
import itertools

result = []
arr = []
while(True) :
    txt = sys.stdin.readline().split()
    if (txt[0] == '0') :
        break

    arr.append(txt)


for i in range(len(arr)):
    n = int(arr[i].pop(0))
    nCr = list(itertools.combinations(arr[i], 6))

    for j in range(len(nCr)):
        print(' '.join(nCr[j]))
    
    if i < len(arr)-1:
        print()