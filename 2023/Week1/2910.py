#빈도 정렬
"""
5 2
2 1 2 1 2

9 77
11 33 11 77 54 11 25 25 33

11 11 11 33 33 25 25 77 54
"""

import collections

n, c = map(int, input().split())
data = list(map(int, input().split()))

counts = collections.Counter(data)
counts = sorted(counts.items(), key=lambda x: x[1], reverse=True)

result = ""
for k,v in counts:
    for j in range(v):
        result += str(k)+" "

print(result)


