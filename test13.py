
def solution(n, times):
    answer = 0
    listed = []
    for i in times:
        listed += [ k * i for k in range(1, n+1)]
    
    listed.sort()

    return listed[n-1]


n = 6
times = [7, 10]
print(solution(n, times))













# 이분 탐색
# 정렬된 값에서 찾음

def binary_search(a, x) :
    start = 0
    end = len(a) - 1

    while start <= end :
        mid = (start + end) // 2
        if x == a[mid] :
            return mid
        elif x > a[mid] :
            start = mid + 1
        else :
            end = mid - 1


    return -1

# d = [1, 4, 9, 16, 25, 36, 49, 64, 81]
# print(binary_search(d, 36))