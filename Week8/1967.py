# 트리의 지름 
# 그래프 탐색
# dfs
"""
12
1 2 3
1 3 2
2 4 5
3 5 11
3 6 9
4 7 1
4 8 7
5 9 15
5 10 4
6 11 6
6 12 10
"""

import sys
sys.setrecursionlimit(10 ** 9)

# dfs 탐색
def dfs(x, y): 
    for a, b in graph[x]:
        if visited[a] == -1:
            visited[a] = y + b 
            dfs(a, y + b)


n = int(sys.stdin.readline())

graph = [[] for _ in range(n + 1)]
for _ in range(n - 1):
    a, b, c = map(int, sys.stdin.readline().split())
    graph[a].append([b, c])
    graph[b].append([a, c])

visited = [-1] * (n + 1) 
visited[1] = 0 
dfs(1, 0) 

start = visited.index(max(visited))

visited = [-1] * (n + 1) 
visited[start] = 0 
dfs(start, 0) 

print(max(visited))