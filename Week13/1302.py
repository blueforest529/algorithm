N = int(input())
books = {}
for i in range(N):
    name = input()
    if name in books.keys() :
        books[name] += 1
    else :
        books[name] = 1

# 키 값 기준으로 오름차순
sorted_dict = dict(sorted(books.items(), key=lambda item: item[0]))

# print(max(sorted_dict, key=sorted_dict.get))