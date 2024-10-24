# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    A.sort()

    for x in range(0, len(A)-2):
        a = A[x]
        b = A[x+1]
        c = A[x+2]
        
        if a+b > c and b+c > a and c+a > b :
            return 1

    return 0
