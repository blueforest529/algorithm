T = int(input())

for i in range(T) :
    x = int(input())
    y = int(input()) 
    pan = [x for x in range(1, y+1)]     
    for k in range(x):
        for i in range(1, y):
            pan[i] += pan[i-1]
    print(max(pan))
    
    
    