# 철도
# 우선순위 큐

"""
8
5 40
35 25
10 20
10 25
30 50
50 60
30 25
80 100
30
"""

import sys
import heapq
input = sys.stdin.readline

hq = []
N = int(input())

for _ in range(N):
    start, end = map(int, input().split())
    if start > end:
        start, end = end, start
    heapq.heappush(hq, (end, start))
    
D = int(input())

possible = []
res = 0
cnt = 0
while hq:
    end, start = heapq.heappop(hq)
    
    if start >= end - D:
        heapq.heappush(possible, (start, end))
        cnt += 1
        
    while possible:
        s, e = heapq.heappop(possible)
   
        if s < end - D:
            cnt -= 1
        
        # 철도의 범위에 해당하면 나머지 요소들도 포함 됨.
        # 따라서 break
        else:
            heapq.heappush(possible, (s, e))
            break
        
    res = max(res, cnt)
    
print(res)
        
    
    
    

