chess = [1,1,2,2,2,8]
inputArr = list(map(int, input().split()))
    
result = list(map(lambda x, y: x - y, chess, inputArr))
print(*result, sep=" ")
