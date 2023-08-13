N = int(input())
arr = list(map(int, input().split()))
Node = int(input())
result = 0

def dfs(Node, arr):    
    arr[Node] = -2
    for i in range(N):
        if Node == arr[i]:
            dfs(i, arr)
            
dfs(Node, arr)

for i in range(N) :
    if arr[i] != -2 and not i in arr:
        result += 1
        
print(result)
