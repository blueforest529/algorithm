"""
RGB거리

3
26 40 83
49 60 57
13 89 99
"""

N = int(input())
board = [list(map(int,input().split())) for _ in range(N)]

for idx, val in  enumerate(board):
    if (idx < N-1) :
        board[idx+1][0] += min(board[idx][1], board[idx][2])
        board[idx+1][1] += min(board[idx][0], board[idx][2])
        board[idx+1][2] += min(board[idx][0], board[idx][1])
        
        
print(min(board[N-1]))
