def solution(arr):
    qu = []
    for i in arr:

        if i not in qu:
            qu.append(i)
        
        else:
            if qu[-1] != i:
                qu.append(i)

    return qu


arr = [1,1,3,3,0,1,1]
print(solution(arr))
