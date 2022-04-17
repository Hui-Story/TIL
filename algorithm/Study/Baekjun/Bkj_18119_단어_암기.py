import sys
input = sys.stdin.readline

N, M = map(int, input().split())

words = [[] for _ in range(26)]

for _ in range(N):
    word_set = set(input().strip())
    word_bit = 0
    for word in word_set:
        word_bit |= 1 << (ord(word) - 97)
    for word in word_set:
        words[ord(word) - 97].append(word_bit)

bit = (1 << 26) - 1

for _ in range(M):
    o, x = map(str, input().split())
    x_idx = ord(x) - 97
    if o == '1':
        for word in words[x_idx]:
            if (bit & word) == word:
                N -= 1
        bit &= ~(1 << x_idx)
    else:
        bit |= (1 << x_idx)
        for word in words[x_idx]:
            if (bit & word) == word:
                N += 1
    print(N)