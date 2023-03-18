# 순차 탐색 알고리즘

def search_list(a, x) :
    n = len(a)
    for i in range(0, n) :
        if x == a[i]:
            return i

    return -1


a = [1,4,5,22,344,12,3,4,2]
print(search_list(a, 3))
print(search_list(a, 222))
