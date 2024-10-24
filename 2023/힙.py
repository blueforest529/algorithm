import heapq

def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)

    if scoville[0] >= K:
        return answer
    
    while scoville[0] < K:
        if len(scoville) == 1:
            return -1

        min_scoville = heapq.heappop(scoville)
        min2_scoville = heapq.heappop(scoville)
        
        heapq.heappush(scoville, min_scoville + min2_scoville*2)
        answer += 1
   
    return answer


scoville = [1, 2, 3, 9, 10, 12]
k = 7
print(solution(scoville, k))