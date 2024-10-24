## 합 구하기

def sum(number):   
    add = 0

    for i in range(1, number+1):
        add += i

    return add

def sum_n(number):
    return number * (number+1) // 2


def squre(number):
    add = 0
    
    for i in range(1, number+1):
        add += i * i
    
    return add

print(sum(10))
print(sum_n(10))
print(squre(10))