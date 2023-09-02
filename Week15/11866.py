import sys
input = sys.stdin.readline
N, M= map(int, input().split())
li = [int(i+1) for i in range(N)]

result = []
num = 0

for i in range(N):
    num += M -1
    if num >= len(li):
        num = num%len(li)
        
    result.append(li.pop(num))
    
print('<', end='')
print(*result, sep=', ', end='>')