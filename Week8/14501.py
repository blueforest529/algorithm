# 퇴사
"""
7
3 10
5 20
1 10
1 20
2 15
4 40
2 200
"""

N = int(input())
Arr = [list(map(int,input().split())) for i in range(N)]

dp = [ 0 for i in range(N+1)]

for i in range(N):
    for j in range(i+Arr[i][0], N+1) :
        if dp[j] < dp[i] + Arr[i][1] :
            dp[j] = dp[i] + Arr[i][1]
            # 초기값 쌓으면서 반복

print(dp[-1])