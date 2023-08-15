"""
5
RRRBB
GGBBB
BBBRR
BBRRR
RRRRR
"""

import sys
sys.setrecursionlimit(1000000)
input = sys.stdin.readline

n = int(input().rstrip())
board = [list(input().rstrip()) for _ in range(n)]
visited = [[False] * n for _ in range(n)]

dx = [-1,1,0,0]
dy = [0,0,-1,1]


# def dfs():
    
print(board)
print(visited)