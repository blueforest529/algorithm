#팩토리얼을 구하는 알고리즘

def fact(num) :
    fact = 1
    for i in range(1, num+1) :
        fact = fact*i
    
    return fact

#재귀 함수

def factr(num) :
    if num <= 1 :
        return 1
    
    return num * factr(num-1)

print(factr(1))
print(factr(5))
print(factr(10))