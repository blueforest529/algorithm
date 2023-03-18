#최소 직사각형

def solution(sizes):
    answer = 0
    x,y = [],[]
    for i in range (len(sizes)):
        x.append(max(sizes[i]))
        y.append(min(sizes[i]))

    answer=max(x)*max(y)

    return answer

sizes = [[14, 4], [19, 6], [6, 16], [18, 7], [7, 11]]
print(solution(sizes))
