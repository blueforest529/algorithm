## 최대값 구하기


num = [17,92,18,33,58,7,33,42]

def max_num():
    max = 0
    for i in num:
        if i > max: 
            max = i 

    return max

def max_idx():
    idx = 0
    for i in range(1, len(num)):
        if num[i] > num[idx]: 
            idx = i
        
    return idx

def min_num():
    min = num[0]
    for i in num:
        if i < min: 
            min = i 

    return min


print(max_num())
print(max_idx())
print(min_num())
