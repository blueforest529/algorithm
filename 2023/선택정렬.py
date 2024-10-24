# 순차정렬알고리즘
# 쉬운 정렬 알고리즘

def find_min(a):
    n = len(a)
    min = 0
    for i in range(1, n):
        if a[i] < a[min] :
            min = i

    return min

def sort_arr(a):
    result = []
    while a:
        min = find_min(a)
        value = a.pop(min)
        result.append(value)

    return result


a = [2,5,3,4,1]
# print(sort_arr(a))


# 일반적인 선택 정렬 알고리즘

def sort2(a) :
    n = len(a)
    for i in range(0, n-1) :
        min = i
        for j in range(i+1, n) :
            if a[j] < a[min] :
                min = j

        #찾은 최소값을 i번째 위치로
        a[i], a[min] = a[min] , a[i]
        #python에서 두 원소 자리 바꿀때

    return a


a = [2,3,5,4,1,5]
print(sort2(a))


def sort3(a) :
    n = len(a)
    for i in range(0, n-1) :
        max = i
        for j in range(i+1, n) :
            if a[j] > a[max] :
                max = j

                #찾은 최대값을 i번째 위치로
        a[i], a[max] = a[max], a[i]
                #python에서 두 원소 자리 바꿀때

    


a = [2,5,3,4,1]
sort3(a)
print(a)
