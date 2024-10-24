#레벨 햄버거
n, x = map(int, input().strip().split())
L1 = "BPPPB"
bugger = 'B'

for i in range(n):
    bugger += L1
    if i < n-1 :
        bugger += 'P'

bugger += 'B'

print(bugger)
# print(bugger[:x])
# print(bugger[:x].count('P'))