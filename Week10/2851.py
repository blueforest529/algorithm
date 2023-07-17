ans = 0
mushroom = []
result = 0
for i in range(10):
    mushroom.append(int(input()))

for i in range(10):
    ans += mushroom[i]
    
    if ans == 100 :
        result = ans
        break
    
    if ans > 100:
        a = ans-100
        b = (ans - mushroom[i]) - 100
      
        if abs(a) <= abs(b):
            result = ans
            break
        else :
            result = ans - mushroom[i]
            break
        
    if i >= 9:
        result = ans



print(result)

    