import sys

A = []
for _ in range(9):
    A.append(int(sys.stdin.readline()))

A.sort(reverse=True)
asum = sum(A)

for i in range(0,8):
    for j in range(i+1,9):
        B = []
        B.append(A[i])
        B.append(A[j])
        bsum = sum(B)
        result = asum - bsum
        if(result == 100): 
            # print(A[i], ", ", A[j])
            # A.pop(i)

            del A[i]
            del A[j-1]
            # A.pop(j-1)
            A.sort()
            break

    if len(A) == 7 :
        break

print("result")


for i in A:
    print(i)

