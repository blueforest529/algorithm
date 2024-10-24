
#프로그래머스 카펫

from itertools import *
def solution(brown, yellow):
    # answer = []
    # x, y = [], []

    # divi = []
    # n = brown + yellow
    # for i in range(1, n+1):
    #     if i == n : continue

    #     if n % i == 0:
    #         divi.append(i)

    # if len(divi) < 3 :
    #     divi = divi + divi

    # x = sorted(list(filter(lambda x : x, divi)))
    # xlist = (list(permutations(x, 2)))

    # for i in xlist :
    #     if i[1] < 3 : continue
    #     if i[1] > i[0]: continue
    #     if i[0] * i[1] == n:
    #         if  (i[0]-2) * (i[1]-2)== yellow :
    #             return list(i)

    for i in range(2,yellow//2+1):
        print(yellow//2)
        if yellow % i ==0 and  (i+ yellow// i)*2+4 == brown:
            return [yellow//i+2, i+2]
    if yellow==1:
         return [3,3]
    elif yellow ==2:
        return [4,3]
    elif yellow ==3:
        return [5,3]
            

    # return answer


brown, yellow = 12, 4
print(solution(brown, yellow))