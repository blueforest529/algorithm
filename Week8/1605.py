#반복 부분문자열
#LCP 알고리즘
"""
28
tellmetellmetetetetetetellme
"""
def build_suffix_array(s):
    n = len(s)
    suffix_array = [0] * n
    rank = [0] * n

    for i in range(n):
        suffix_array[i] = i
        rank[i] = ord(s[i]) #유니코드 변환

    arr = []
    k = 1
    while k < n:
        #순서가 동일 하면 후순위로
        suffix_array.sort(key=lambda x: (rank[x], rank[(x + k) % n]))
   
        new_rank = [0] * n
        new_rank[suffix_array[0]] = 0
        
        for i in range(1, n):
            if rank[suffix_array[i]] == rank[suffix_array[i - 1]] \
                and rank[(suffix_array[i] + k) % n] == rank[(suffix_array[i - 1] + k) % n]:
                
                new_rank[suffix_array[i]] = new_rank[suffix_array[i - 1]]
            else:
                new_rank[suffix_array[i]] = new_rank[suffix_array[i - 1]] + 1

            arr.append(chr(suffix_array[i]))
            
        rank = new_rank
       
        k *= 2
    
    print(arr)
     
    return suffix_array

def build_lcp_array(s, suffix_array):
    n = len(s)
    lcp_array = [0] * n
    lcp = 0
    inv_suffix_array = [0] * n

    for i in range(n):
        inv_suffix_array[suffix_array[i]] = i

    for i in range(n):
        if inv_suffix_array[i] == n - 1:
            lcp = 0
        else:
            j = suffix_array[inv_suffix_array[i] + 1]
            while i + lcp < n and j + lcp < n and s[i + lcp] == s[j + lcp]:
                lcp += 1
            lcp_array[inv_suffix_array[i]] = lcp
            if lcp > 0:
                lcp -= 1

    return lcp_array

L = '28'
string = 'tellmetellmetetetetetetellme'

suffix_array = build_suffix_array(string)
lcp_array = build_lcp_array(string, suffix_array)

result = max(lcp_array)
print(result)
