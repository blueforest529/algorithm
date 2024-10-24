"""
10 4200
1
5
10
50
100
500
1000
5000
10000
50000
"""
N, K = map(int, input().split()) 
coinList = list()
for i in range(N):
    coin = int(input())
    if K >= coin :
        coinList.append(coin)
        
result = 0
for i in sorted(coinList,reverse=True):
    if K >= i:
        a, b = divmod(K, i)
        result+= a
        K = b     
        
print(result)

    
    