# def solution(a, b):
#     answer = 0
    
#     if a == b:
#         return a

#     if a > b :
#         a, b = b, a

#     for i in range(a, b+1) :
#         answer += i

#     return answer


# a = 5
# b = 3

# print(solution(a, b))


def solution(x):
    answer = True
    sumdata = sum(map(int, str(x)))
    print(sumdata)
    
    if x % sumdata != 0 :
        answer = False
    

    return answer

arr = 13
print(solution(arr))