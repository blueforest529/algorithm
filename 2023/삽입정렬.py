#삽입 정렬

def find_ins_idx(r, v) :
    for i in range(0, len(r)):
        if v < r[i] :
            return i
            
    return v


def ins_sort(a):
    result = []
    while a:
        value = a.pop(0)
        ins_idx = find_ins_idx(result, value)
        result.insert(ins_idx, value)
        # print(a, result)
    
    return result

d = [5,2,7,3,1,8,9,2]
# print(ins_sort(d))


#일반적인 삽입 정렬

def ins_sort2(a):
    n = len(a)

    for i in range(1, n):
        key = a[i]
        j = i-1

        while j >= 0 and a[j] > key :
            a[j+1] = a[j]
            j -= 1
            print('1 =',a)
        
        a[j+1] = key
    

d = [5,2,7,3,1,8,9]
ins_sort2(d)
print(d)