# 역삼역
# banana

# n, k = map(int,input().split())
# string = input()
n = 6
k = 3
string = 'banana'

substrings = set()
Arr = set()
result = set()
count = 0

for i in range(n):
    for j in range(i+1, n+1):
        s = string[i:j]
        Arr.add(s)
        
        if len(s) < k :
            continue
        
        if s == s[::-1]:
            substrings.add(string[i:j])

for i in substrings:
    for j in Arr :
        if i in j : 
            result.add(j)   
            
print(len(result))
