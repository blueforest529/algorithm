"""
패션왕 신혜빈
2
3
hat headgear
sunglasses eyewear
turban headgear
3
mask face
sunglasses face
makeup face
"""

resultArr = []
N = int(input())
for i in range(N):
    kind = int(input())
    clothes_dict = {}
    cloth = {}
    
    for j in range(kind) :
        cloth, category = input().split()
        
        if (category in clothes_dict.keys()):
            clothes_dict[category] += [cloth]
        else :
            clothes_dict[category] = [cloth, ""]

    answer = 1
    for key in clothes_dict.keys():
        answer *= len(clothes_dict[key])
    resultArr.append(answer-1)
    
        
print(*resultArr, sep="\n")     
        