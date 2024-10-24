# 인구 이동
# bfs
"""
2 20 50
50 30
20 40
"""
from collections import deque

n, l, r = map(int,input().split())
rand = [list(map(int,input().split())) for i in range(n)]

# 상하좌우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(x, y, idx) :
    # 연합사이 연결 되어있는지 체크
    united = []
    united.append((x,y))
    q = deque()
    q.append((x,y))

    # 연합에게 임의의 숫자 할당 하고 인구수 체크
    union[x][y] = idx
    summary = rand[x][y]
    count = 1
    
    while q :
        x, y = q.popleft()
        for i in range(4) :
            nx = x + dx[i]
            ny = y + dy[i]
            # 옆 나라와 인원 수 체크
            if 0 <= nx < n and 0 <= ny < n and union[nx][ny] == -1:
                #만족하면 추가 
                if l <= abs(rand[nx][ny] - rand[x][y]) <= r:
                    q.append((nx,ny))
                    union[nx][ny] = idx
                    summary += rand[nx][ny]
                    count += 1
                    united.append((nx,ny))
    
    for i, j in united:
        rand[i][j] = summary // count
    
    return count

result = 0

while 1:
    union = [[-1] * n for _ in range(n)]
    idx = 0
    for i in range(n):
        for j in range(n):
            if union[i][j] == -1:
                bfs(i, j, idx)
                idx += 1
    
    if idx == n * n:
        break
    
    result += 1

print(result)