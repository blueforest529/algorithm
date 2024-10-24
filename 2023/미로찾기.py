# 미로 찾기 프로그램

def solve_maze(g, start, end) :
    qu = [] # 이동 경로
    done = set() # 중복 방지 

    qu.append(start)
    done.add(start)

    while qu:
        p = qu.pop(0)
        v = p[-1]

        if v == end : # 도착지니?
            return p

        for x in g[v]: # 연결된 꼭짓점 중에 
            if x not in done: # 큐에 추가 된 적 없는 꼭짓점을
                qu.append(p+x) # 추가
                done.add(x)

    return "?" # 도착점이 안나오면 나갈 수 없는 미로



maze = {
    'a' : ['e'],
    'b' : ['c', 'f'],
    'c' : ['b', 'd'],
    'd' : ['c'],
    'e' : ['a', 'i'],
    'f' : ['b', 'g', 'j'],
    'g' : ['f', 'h'],
    'h' : ['g', 'l'],
    'i' : ['e', 'm'],
    'j' : ['f', 'k', 'n'],
    'k' : ['j', 'o'],
    'l' : ['h', 'p'],
    'm' : ['i', 'n'],
    'n' : ['m', 'j'],
    'o' : ['k'],
    'p' : ['l']
}

print(solve_maze(maze, 'a', 'p'))