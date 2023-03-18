from collections import deque

def solution(priorities, location):
    answer = 0 

    qu = deque([(v,i) for i,v in enumerate(priorities)])
    # print(qu)

    maxidx = max(qu)[0]
    # print(maxidx)

    while len(qu):
        print(qu)
        item = qu.popleft()
        if qu and max(qu)[0] > item[0]:
            qu.append(item)
        
        else :
            answer += 1
            if item[1] == location :
                break

    return answer

# def solution(priorities, location):
#   answer = 0
#   from collections import deque

#   d = deque([(v,i) for i,v in enumerate(priorities)])

#   while len(d):
#       item = d.popleft()
#       if d and max(d)[0] > item[0]:
#           d.append(item)
#       else:
#           answer += 1
#           if item[1] == location:
#               break
#   return answer


prioritie = [2, 0, 0, 0, 0]
location = 4
print(solution(prioritie, location))