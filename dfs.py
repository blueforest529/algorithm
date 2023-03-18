#네트워크

def solution(n, computers):
    answer = 0
    visited = [False for x in range(0, n)]
    for i in range(0, n):
        if visited[i] == False:
            dfs(n, i, visited,computers)
            answer+=1

    return answer

def dfs(n, i, visited, computers):
    visited[i]=True
    for j in range(n):
        if i!=j and computers[i][j]==1:
            if visited[j]==False:
                dfs(n,j,visited,computers)

n = 3
computers = [[1, 1, 0], [1, 1, 0], [0, 0, 1]]
solution(n, computers)
print(solution(n, computers))