# def solution(citations):
#     answer = 0
#     citations.sort(reverse=True)

#     for idx, val in enumerate(citations):
#         if idx >= val:
#             return idx
        
#     return len(citations)

# citations = [3, 0, 6, 1, 5]
# # solution(citations)
# print(solution(citations))

## 내꺼

# from itertools import *

# def solution(numbers):
#     answer = ''
#     length = len(numbers)
#     arr = list(permutations(numbers, length))
#     max = 0
#     for i in arr:
#         txt = ""
#         for j in i:
#             txt += str(j)
        
#         if max < int(txt):
#             max = int(txt)

#     answer = str(max)
#     return answer

from itertools import *

def solution(numbers):
    answer = ''

    num = list(map(str, numbers))
    print(num)
    num.sort(key = lambda x : x*3, reverse = True)
    return str(int(''.join(num)))


numbers = [3, 30, 34, 5, 9]	
# solution(numbers)
print(solution(numbers))
