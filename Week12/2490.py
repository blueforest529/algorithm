#윷놀이
"""
0 1 1 1
0 0 1 1
0 0 0 1
0 0 0 0
1 1 1 1
"""
result = []
for i in range(3) :
    n = list(map(int, input().split())).count(1)
    result.append(int(n))

for i in result :
    if i == 4:
        print('E')
    else :
        print(chr(64+(4-i)))
    
