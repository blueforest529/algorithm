"""
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

N = int(input())
for i in range(N):
    kind = int(input())
    for j in range(kind) :
        cloth, category = input().split()
        
        