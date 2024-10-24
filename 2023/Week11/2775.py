"""
2
1
3
2
3
"""

T = int(input())

for i in range(T) :
    x = int(input())
    y = int(input()) 
    pan = [x for x in range(1, y+1)]    

    for k in range(x):
        for i in range(1, y):
            pan[i] += pan[i-1]
        print(pan)
    print(max(pan))
    
"""    
T = int(input())
n = 5
arr = []
pan = [x for x in range(1, n+1)]
xy = []

for i in range(T) :
    x = int(input())  # 층
    y = int(input())  # 호
    xy.append([x,y])

for k in range(n):
    arr.append([1])
    for i in range(1, n):
        pan[i] += pan[i-1]
        arr[k].append(pan[i])

for i in xy :
    X = i[0] -1
    Y = i[1] -1 
    print(arr[X][Y])
    """