import sys
input = sys.stdin.readline

N = int(input())
word_cnt = [[[i, 0] for i in range(10)] for _ in range(12)]
used = [0]*10
not_zero = [0]*10
word_check = [0]*10
max_word_len = 0
result = 0

for _ in range(N):
    inp = str(input().strip())
    max_word_len = max(max_word_len, len(inp))
    for i in range(len(inp)):
        if i == 0:
            not_zero[ord(inp[i])-65] = 1
        word_cnt[len(inp)-1-i][ord(inp[i])-65][1] += 1
        word_check[ord(inp[i])-65] = 1

not_zero_cnt = sum(not_zero)
word_check = sum(word_check)

for num in range(9, -1, -1):
    max_sum = -1
    now_word = 0
    for word_ord in range(10):
        if used[word_ord]:
            continue
        if num and not_zero_cnt == num and not not_zero[word_ord]:
            continue
        tmp = 0
        for i in range(max_word_len):
            tmp += num * word_cnt[i][word_ord][1] * (10**i)
        if tmp > max_sum:
            max_sum = tmp
            now_word = word_ord
    result += max_sum
    used[now_word] = 1
    if not_zero[now_word]:
        not_zero_cnt -= 1

print(result)