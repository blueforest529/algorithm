import sys
input = sys.stdin.readline
N = int(input())

if N < 3:
    print(1)
    sys.exit()

dp = [0 for _ in range(N)]

dp[0] = 1
dp[1] = 1
dp[2] = 2

for i in range(3, N):
    dp[i] = dp[i-2] + dp[i-1]
    
print(dp[N-1])