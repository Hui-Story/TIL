import sys
input = sys.stdin.readline

N = int(input())

word_len = [[] for _ in range(51)]

for _ in range(N):
    word = input().strip()
    word_len[len(word)].append(word)

for i in range(1, 51):
    if word_len[i]:
        word_len[i] = sorted(list(set(word_len[i])))

for i in range(1, 51):
    for word in word_len[i]:
        print(word)