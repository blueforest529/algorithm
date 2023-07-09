# 팰린드롬
# abacaba

# S = input()
S = 'abacaba'
result = []

def find_all_palindromes(string):
    palindromes = []
    length = len(string)

    # 길이 1인 팰린드롬 추가
    for i in string:
        if (i not in palindromes) : 
            palindromes.append(i)
            result.append(S.count(i))
        
    # 길이 2 이상인 팰린드롬 추가
    for i in range(length):
        for j in range(i+2, length+1):
            substring = string[i:j]
            if substring == substring[::-1]:
                result.append(S.count(substring) * len(substring))

    print(max(result))

find_all_palindromes(S)

