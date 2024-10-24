#최대 공약수 구하기

def gcd(a,b) :
    i = min(a,b) #두 숫자 중 작은 수 찾는 함수
    while True :
        if a%i == 0 and b%i == 0 : 
            return i
        i = i-1


#유클리드 공식으로 최대 공략수 구하기
def gcdr(a, b) :
    if b == 0:
        return a
    return gcdr(a, a%b)

print(gcd(1, 5))
print(gcd(8, 16))
print(gcd(4, 20))


print(gcdr(25, 40))
print(gcdr(8, 16))
print(gcdr(4, 20))
