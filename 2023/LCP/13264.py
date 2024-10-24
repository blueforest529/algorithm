# 접미사 배열2
# abcdabcabb

S = "abcdabcabb"
N = len(S)
suffix_array = [0] * N
rank = [0] * N

for i in range(N) :
    suffix_array[i] = i
    rank[i] = ord(S[i])

k = 1
while k < N:
    suffix_array.sort(key=lambda x: (rank[x], rank[(x + k) % N]))
    new_rank = [0] * N
    new_rank[suffix_array[0]] = 0

    for i in range(1, N):
        if rank[suffix_array[i]] == rank[suffix_array[i - 1]] \
            and rank[(suffix_array[i] + k) % N] == rank[(suffix_array[i - 1] + k) % N]:
            new_rank[suffix_array[i]] = new_rank[suffix_array[i - 1]]
        else:
            new_rank[suffix_array[i]] = new_rank[suffix_array[i - 1]] + 1

    rank = new_rank
    k *= 2

print(*suffix_array, sep="\n")

