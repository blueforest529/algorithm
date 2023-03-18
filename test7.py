def solution(s):
    answer = ''
    arr = s.split()
    d1 = min(arr) #max
    d2 = max(arr) #min

    for i in arr:
        if int(d1) < int(i) :
            d1 = i
        
        if int(d2) > int(i) :
            d2 = i
        
    answer = str(d2)+" "+str(d1)
    return answer



s = "-1 -1"

print(solution(s))