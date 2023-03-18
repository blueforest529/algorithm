import itertools

def solution(A, B, C):
    #print(A, B, C)
    # Implement your solution here


    x = bin(A)[2:]
    y = bin(B)[2:]
    z = bin(C)[2:]

    print(x, y, z);

    xflag = []
    for i in [i for i, c in enumerate(x) if c == '0']:
        i = 2 ** (29 - int(i))
        xflag.append(i)

    print(xflag)

    

    #return ""


A = 1073741727
B = 1073741631
C = 1073741679

solution(A,B,C)


