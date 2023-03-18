#퀵 알고리즘

# def quick_sort(a):
#     n = len(a)

#     if n <= 1:
#         return a

#     pivot = a[-1]
#     g1 = []
#     g2 = []

#     for i in range(0, n-1) :
#         if a[i] < pivot :
#             g1.append(a[i])
#         else :
#             g2.append(a[i])


#     return quick_sort(g1) + [pivot] + quick_sort(g2)

# d = [6,8,3, 9, 10, 1, 2,4, 7, 5]
# # d = [6,8,3, 9, 10, 5, 2,4, 7,1]
# print(quick_sort(d))



# 정렬 범위를 지정해서 알려줌
def quick_sort2(a, start, end):
    if end - start <= 0 :
        return
    
    pivot = a[end]
    i = start

    for j in range(start, end):
        if a[j] <= pivot :
            a[i], a[j] = a[j], a[i]
            i += 1
    
    a[i], a[end] = a[end], a[i]

    quick_sort2(a, start, i-1)
    quick_sort2(a, i+1, end)

def quick_sort22(a) :
    quick_sort2(a, 4, len(a)-1)



d = [6,8,3, 9, 10, 1, 2,4, 7, 5]
# d = [6,8,3, 9, 10, 5, 2,4, 7,1]
quick_sort22(d)
print(d)
