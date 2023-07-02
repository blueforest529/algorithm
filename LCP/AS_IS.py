# 접미사 배열 만들기
def print_suffixes(S):
    suffixes = []
    for i in range(len(S)):
        suffixes.append((S[i:], i+1))
    suffixes.sort()
    for suffix, index in suffixes:
        print(f"{index}: {suffix}")


S = "banana"
S = "abracadabra"
print_suffixes(S)
