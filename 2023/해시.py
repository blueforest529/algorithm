# from collections import deque

# def solution(s):
#     answer = True
#     st = []
#     for x in s:
#         if x == '(':
#             st.append(x)
#         elif st and x == ')':
#             st.pop()
#         else:
#             answer = False
#             break
    
#     if len(st) != 0 :
#         answer = False

#     return answer


# s = "()))))"
# print(solution(s))

from itertools import permutations

def solution(clothes):
    dict3 = dict()

    for i in range(0, len(clothes)):
        key = clothes[i][1]
        if dict3 and key in dict3 :
            l = [clothes[i][0]]
            dict3[key] += l


        else : 
            dict3[key] = [clothes[i][0]]

    result = 1

    for key in dict3.keys():
        result = result * (len(dict3[key]) + 1)

    return result-1



clothes = [["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["blue_sunglasse2s", "eyewear"],["blue_sungl", "wewq"], ["green_turban", "headgear"]]
print(solution(clothes))


