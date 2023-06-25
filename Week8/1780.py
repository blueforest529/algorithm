#종이의 개수
"""
9
0 0 0 1 1 1 -1 -1 -1
0 0 0 1 1 1 -1 -1 -1
0 0 0 1 1 1 -1 -1 -1
1 1 1 0 0 0 0 0 0
1 1 1 0 0 0 0 0 0
1 1 1 0 0 0 0 0 0
0 1 -1 0 1 -1 0 1 -1
0 -1 1 0 1 -1 0 1 -1
0 1 -1 1 0 -1 0 1 -1
"""


def dfs(x, y, z):
    global answer
    visited = papers[x][y]

    for i in range(x, x + z):
        for j in range(y, y + z):
            # 시작점에 종이의 숫자가 현재 종이의 숫자와 다르다면
            if papers[i][j] != visited:
                # 3 * 3 범위를 재귀적으로 탐색
                for k in range(3):
                    for l in range(3):
                        dfs(x + k * z // 3, y + l * z // 3, z // 3)
                return

    if visited == -1:
        answer[0] += 1
    elif visited == 0:
        answer[1] += 1
    else:
        answer[2] += 1


N = int(input())
papers = [[int(x) for x in input().split()] for y in range(N)]
answer = [0, 0, 0]
dfs(0, 0, N)

for i in answer:
    print(i)


