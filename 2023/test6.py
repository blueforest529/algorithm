answer =[]

def hanoi(n, from_, to, mid):
    if n == 1:
        answer.append([from_, to])
        # print(from_, " -> ", to)
        return 
    
    hanoi(n-1, from_, mid, to)
    # print(from_, " -> ", to)
    answer.append([from_, to])
    hanoi(n-1, mid, to, from_)


def solution(n):
    # answer = []
    # print(int(n))
    # hanoi = [i for i in range(1, n+1)]

    # print(hanoi)

    # hanoi(n)


    print("n = 1")
    hanoi(n, 1, 3, 2)
    print(answer)
    # print("n = 2")
    # (hanoi(2, 1, 3, 2))
    # print("n = 3")
    # (hanoi(3, 1, 3, 2))

    # if n == 1:
    #     print(from_, " -> ", to)
    #     return 
    # (hanoi(1, 1, 3, 2))
    # hanoi(n-1, from_, mid, to)
    # print(from_, " -> ", to)
    # hanoi(n-1, mid, to, from_)

    # if n == 1:
    #     # print()
    #     return 
    
    # solution(n, from_, mid, to)
  

    return answer


solution(2)

