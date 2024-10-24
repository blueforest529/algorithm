#절댓값 힙
import heapq
import sys

n = int(sys.stdin.readline())
arr = []
heap = []

for i in range(n):
    n = int(sys.stdin.readline())
    arr.append(n)

for i in range(len(arr)):
    if arr[i] != 0 :
        res = (abs(arr[i]), arr[i])
        heapq.heappush(heap, res)

    else : 
        if heap :
            print(heapq.heappop(heap)[1])
        else :
            print(0)
