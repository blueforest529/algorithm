"""
4 4
3 0 1 4
"""

x, y = map(int,input().split())
graph = list(map(int,input().split()))


ans = 0
# for i in range(1, y+1):
#     for j in range(i+1, y+1):
#         ii =  graph[i]
#         jj =  graph[j]
#         if ii < jj:
#             ans += (jj-ii) * jj
#             print(ans)
        
        
for i in range(1, y - 1):
    left_max = max(graph[:i])
    right_max = max(graph[i+1:])

    compare = min(left_max, right_max)

    if graph[i] < compare:
        ans += compare - graph[i]
        

print(ans)