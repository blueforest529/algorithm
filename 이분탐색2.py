
def solution(n, times):
    answer = 0
    left = 0
    right = 1024 # 일단 무조건 큰 수로

    while left <= right:
        interval_sum = 0
        mid = (left+right)//2

        for i in times:
            interval_sum += mid//i
            if interval_sum >= n:
                right = mid - 1
                answer = mid
                break

        if interval_sum < n :
            left = mid + 1

    return answer


n = 6
times = [7, 10]

# n=7
# times=[10,10]

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