##BFS
from collections import deque

def solution(numbers, target):
    answer = 0
    queue = deque([(0, 0)]) # sum, level
    while queue:
        s, l = queue.popleft()
        if l > len(numbers):
            break
        elif l == len(numbers) and s == target:
            answer += 1

        queue.append((s+numbers[l-1], l+1))
        queue.append((s-numbers[l-1], l+1))

    return answer

numbers = [4, 1, 2, 1]
target = 4
print(solution(numbers, target))

## DFS
answer = 0

def solution2(numbers, target):
    dfs(0, 0, numbers, target)
    return answer

def dfs(n, sum, numbers, target):
    global answer
    if n == len(numbers):
        if sum == target:
            answer += 1

        return answer
    
    dfs(n+1, sum+numbers[n], numbers, target)
    dfs(n+1, sum-numbers[n], numbers, target)


numbers = [4, 1, 2, 1]
target = 4
print(solution2(numbers, target))