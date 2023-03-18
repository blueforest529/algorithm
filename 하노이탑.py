#하노이탑 만들기



# n -> 하노이탑 갯수
# from_ -> 출발지
# mid -> 거쳐가는 곳
# to -> 도착지
def hanoi(n, from_, to, mid):
    if n == 1:
        print(from_, " -> ", to)
        return 
    
    hanoi(n-1, from_, mid, to)
    print(from_, " -> ", to)
    hanoi(n-1, mid, to, from_)


print("n = 1")
(hanoi(1, 1, 3, 2))
print("n = 2")
(hanoi(2, 1, 3, 2))
print("n = 3")
(hanoi(3, 1, 3, 2))


