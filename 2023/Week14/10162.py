import copy 
#5분 , 1분, 10초
timeArr = [300, 60, 10]
time = int(input())
timeOrigin = copy.deepcopy(time) 
resultArr = [0, 0, 0]
sum = 0

for i in range(3):
    if time < timeArr[i]:
        continue
    
    a, b = divmod(time, timeArr[i])
    time = b
    resultArr[i] = a
    
    sum += timeArr[i] * resultArr[i]
    
if sum == timeOrigin :
    print(*resultArr, sep=" ")
else :        
    print(-1)

