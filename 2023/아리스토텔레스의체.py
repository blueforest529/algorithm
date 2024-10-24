# from itertools import *

# def solution(numbers):
#     answer = 0
#     arr2 = [x for x in numbers]
#     num = set(permutations(numbers, len(numbers)))
#     arr = []

#     for i in num:
#         if len(i) > 1:
#             txt = ""
#             for j in i:
#                 txt += j
#             arr.append(txt)
#         else :
#             arr.append(i)

#     new_arr = arr + arr2

#     for i in new_arr :
#         if int(i) > 2 :
#             for x in range(2, int(i)-1):
#                 if int(i) % int(x) == 1:
#                     answer+=1
#                     break

#     return answer


# numbers = "011"
# # solution(numbers)
# print(solution(numbers))



    # start = 0
    # end = len(a) - 1

    # while start <= end :
    #     mid = (start + end) // 2
    #     if x == a[mid] :
    #         return mid
    #     elif x > a[mid] :
    #         start = mid + 1
    #     else :
    #         end = mid - 1


# from itertools import permutations
# def solution(n):
#     a = set()
        
#     for i in range(len(n)):
#         a |= set(map(int, map("".join, permutations(list(n), i + 1))))

#     a -= set(range(0, 2))

#     for i in range(2, int(max(a) ** 0.5) + 1):
#         a -= set(range(i * 2, max(a) + 1, i))
   
#     return len(a)

# numbers = "011"
# # solution(numbers)
# print(solution(numbers))


# 아리스토텔레스의 체
n = 100
a = [True] * (n + 1)
m = int(n**0.5)

for i in range(2, m + 1):
    if a[i] == True:
        for j in range(i + i, n + 1, i):
            a[j] = False

print([i for i in range(2, n + 1) if a[i] == True])