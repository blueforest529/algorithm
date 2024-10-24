# 케빈 베이컨의 6단계 법칙
'''
5 5
1 3
1 4
4 5
4 3
3 2

result
3

bfs 알고리즘
'''

import sys
input = sys.stdin.readline
from collections import deque

n, m = map(int, input().strip().split())
graph = [[] for _ in range(n + 1)]
res = []
queue = deque()

# 무방향 그래프
for _ in range(m):
    a, b = map(int, input().strip().split())
    graph[a].append(b)
    graph[b].append(a)

#[[], [3, 4], [3], [1, 4, 2], [1, 5, 3], [4]]

def bfs(i) :
    visited = [0] * (n+1)
    queue.append(i)
    visited[i] = 1

    while queue:
        t = queue.popleft()
        for v in graph[t]:
            if not visited[v]:
                visited[v] = visited[t]+1
                queue.append(v)

    return sum(visited)


for i in range(1, n + 1):
    res.append(bfs(i))

print(res.index(min(res))+1)
