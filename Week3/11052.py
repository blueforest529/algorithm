#카드 구매하기
'''
4
1 5 6 7

result
10
'''

N = int(input())
p = [0] + list(map(int,input().split()))
card = [0 for _ in range(N+1)]

print(p)
print(card)

for i in range(1,N+1):
    for k in range(1,i+1):
        card[i] = max(card[i], card[i-k] + p[k])

# print(max(card))