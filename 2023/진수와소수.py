import math

def solution(n, k):
    answer = 0

    rev_base = '' # 진수 변환
    while n > 0:
        n, mod = divmod(n, k)
        rev_base += str(mod)

    text = rev_base[::-1].split('0') #진수가 역순이여서 변환

    for i in text :
        if len(i) == 0 :
            continue
 
        i = int(i)
        if i < 2 :
            continue

        sosu=True
        for j in range(2,int(i**0.5)+1): # 소수찾기
            if i%j == 0:
                sosu=False
                break
        print(i, sosu)
        if sosu:
            answer+=1
                
    return answer


n = 437674
k = 3

# solution(n, k)
print(solution(n, k))