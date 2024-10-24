"""
바이러스
7
6
1 2
2 3
1 5
5 2
5 6
4 7
"""

N = int(input())
M = int(input())
graph = [[] for _ in range(N+1)]	

for i in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)	
visited = [False] * (N+1)

def DFS(v):
    visited[v] = True
    for i in graph[v]:
        if not visited[i]:
            DFS(i)
    
DFS(1)
print(visited.count(True) - 1)