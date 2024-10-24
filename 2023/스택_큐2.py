from collections import deque

def solution(priorities, location):
    answer = 0 
    qu = deque([(v,i) for i,v in enumerate(priorities)])
    print(qu)

    while len(qu):
        item = qu.popleft()
        
        if qu and max(qu)[0] > item[0]:
            qu.append(item)
        
        else :
            answer += 1
            if item[1] == location :
                break

    return answer

priorities, location = [2, 1, 3, 2], 2
print(solution(priorities, location))