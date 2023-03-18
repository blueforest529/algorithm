from itertools import *
def solution(numbers):
    answer = 0
    numa = []
    for i in range(0, len(numbers)) :
        numa.append(list(map(int, list(map(''.join,  permutations(map(str, numbers), i+1))))))

    num = set(sum(numa, []))
    n = int(max(num))
    a = [False,False] + [True]*(n-1)
    primes=[]

    for i in range(2,n+1):
        if a[i]:  
            primes.append(i)
            for j in range(2*i, n+1, i):
                a[j] = False

    for i in num:
        if int(i) in primes:
            print(int(i))
            answer += 1

    return answer


numbers = "011"
print(solution(numbers))