
import heapq
## 내꺼
def solution(operations):
    dic = [x.split(" ") for x in operations]
    max_list = []
    min_list = []

    for i in dic :
        if i[0] == 'I':
            heapq.heappush(min_list, int(i[1]))
            heapq.heappush(max_list, (-int(i[1]), int(i[1])))
        
        if len(min_list) == 0:
            continue

        if i[0] == "D":
            if i[1] == '1':
                heapq.heappop(max_list)
                min_list.pop()
                
            else:
                heapq.heappop(min_list)
                max_list.pop()
               

    if len(min_list) == 0 : 
        return [0,0]
    else :
        return [max_list[0][1], min_list[0]]

# def solution(operations):
#     min_heap = []
#     max_heap = []
#     for i in operations:
#         if i[0] == 'I':
#             heapq.heappush(min_heap, int(i[1:]))
#             heapq.heappush(max_heap, (-int(i[1:]), int(i[1:])))
#         elif len(min_heap) == 0:
#             continue
#         elif int(i[1:]) == 1:
#             heapq.heappop(max_heap)
#             min_heap.pop()
#         else:
#             heapq.heappop(min_heap)
#             max_heap.pop()
#     if len(min_heap) > 0:
#         return [max_heap[0][1], min_heap[0]]
#     else:
#         return [0, 0]

operations = ["I 16", "I -5643", "D -1", "D 1", "D 1", "I 123", "D -1"]
print(solution(operations))