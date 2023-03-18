from collections import deque
import math

def solution(progresses, speeds):
    answer = []
    qu = deque()
    for idx, progress in enumerate(progresses):
        need_day = math.ceil((100 - progress) / speeds[idx]) # 반올림
        qu.append(need_day)

    # print(qu)
    idx = 0
    stand = qu.popleft()
    answer.append(1)
    while qu:
        vigyo = qu.popleft()
        if vigyo <= stand :
            answer[idx] += 1
        else : 
            stand = vigyo
            answer.append(1)
            idx += 1

    return answer


# progresses = [93, 30, 55]
# speeds =  [1, 30, 5]
progresses = [95, 90, 99, 99, 80, 99]
speeds =  [1, 1, 1, 1, 1, 1]
# progresses = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10]
# speeds =  [10, 10, 10, 10, 10, 10, 10, 10, 10, 10]
# progresses = [1, 1, 50]
# speeds = [100, 2, 1]
# [1,2]

# solution(progresses, speeds)
print(solution(progresses, speeds))
