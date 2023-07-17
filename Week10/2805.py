#나무자르기
"""
4 7
20 15 10 17
"""
n,m = map(int,input().split())
trees = list(map(int,input().split()))
l,r = 1, max(trees)
result = 0 
while l <= r:
    mid = (l + r) // 2
    cnt = 0
    for tree in trees:
        if tree > mid:
            cnt += tree-mid
            
    if cnt >= m :
        l = mid+1
    else :
        r = mid-1
        
print(r)
            


