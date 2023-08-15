"""
5
ABC*+DE/-
1
2
3
4
5
"""

N = int(input())
modify = input()
numArr = []

stack = []  
for i in range(N):
    numArr.append(int(input()))
    

for i in modify:
    if i.isalpha():
        stack.append(numArr[ord(i)-65])
    else :
        str2 = stack.pop()		# stack 리스트의 마지막 2항목을 꺼내와서 계산한다.
        str1 = stack.pop()

        if i =='+' :
            stack.append(str1+str2)
        elif i == '-' :
            stack.append(str1-str2)
        elif i == '*' :
            stack.append(str1*str2)
        elif i == '/' :
            stack.append(str1/str2)


print(f"{stack[0]:.2f}")

# print(numArr)