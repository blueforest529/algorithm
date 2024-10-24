"""
섬의 개수

1 1
0
2 2
0 1
1 0
3 2
1 1 1
1 1 1
5 4
1 0 1 0 0
1 0 0 0 0
1 0 1 0 1
1 0 0 1 0
5 4
1 1 1 0 1
1 0 1 0 1
1 0 1 0 1
1 0 1 1 1
5 5
1 0 1 0 1
0 0 0 0 0
1 0 1 0 1
0 0 0 0 0
1 0 1 0 1
0 0

"""
import sys
sys.setrecursionlimit(10000)


def dfs(grid, i, j):
    if i < 0 or i >= h or j < 0 or j >= w or grid[i][j] != 1:
        return 0
    
    grid[i][j] = 0

    dfs(grid, i+1, j) 
    dfs(grid, i-1, j) 
    dfs(grid, i, j+1) 
    dfs(grid, i, j-1) 
    

while 1:
    w, h = map(int, input().split())
    if w == h == 0:
        break
    
    grid = [list(map(int, input().split())) for _ in range(h)]
    
    count = 0
    for i in range(h) : 
        for j in range(w) :
            if grid[i][j] == 1 :
                dfs(grid, i, j) 
                count += 1
                
    print(count)
                
            