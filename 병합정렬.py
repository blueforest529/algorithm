#병합 정렬
#쪼갤 수 있는 만큼 쪼갬

def merge_sort(a):
    n = len(a)

    print("n : ", n)

    #종료조건 : 정렬한 리스트의 자료개수가 한개 이하면 끝
    if n <= 1:
        return a
    
    mid = n // 2

    print("mid : ", mid)

    g1 = merge_sort(a[:mid])
    g2 = merge_sort(a[mid:])

    print(g1, g2)

    # print(g1, g2)
    result = []
    while g1 and g2:
        if g1[0] < g2[0] :
            result.append(g1.pop(0))
        else:
            result.append(g2.pop(0))
        
    ##이미 빈 배열이 있을수 있음
    while g1:
        result.append(g1.pop(0))
    
    while g2:
        result.append(g2.pop(0))
    
    print("result : ", result)

    return result


d = [8,6,3,9,10,1,2,4,7,5]
merge_sort(d)

# def test(a) :
#     n = len(a)
#     print("n : ", n)

#     #종료조건 : 정렬한 리스트의 자료개수가 한개 이하면 끝
#     if n <= 1:
#         return a
    
#     mid = n // 2

#     print(mid)
#     # print(a[:mid])
#     g1 = test(a[:mid])
#     g2 = test(a[mid:])

#     print(g1, g2)

# test(d)

def merge_sort2(a) :
    n = len(a)

    if n<=1 :
        return
    
    mid = n // 2
    g1 = a[:mid]
    g2 = a[mid:]

    merge_sort2(g1)
    merge_sort2(g2)

    i1 = 0
    i2 = 0

    ia = 0
    while i1 < len(g1) and i2 < len(g2) :
        if g1[i1] < g2[i2] :
            a[ia] = g2[i1]
            i1 += 1
            ia += 1
        else :
            a[ia] = g2[i2]
            i2 += 1
            ia += 1

    while i1 < len(g1):
        a[ia] = g1[i1]
        i1 += 1
        ia += 1

    while i2 < len(g2):
        a[ia] = g1[i2]
        i2 += 1
        ia += 1

