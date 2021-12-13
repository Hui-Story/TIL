N = int(input())
words = [0] * 26
for _ in range(N):
    word = str(input())
    for i in range(len(word)-1, -1, -1):
        words[ord(word[i]) - 65] += 10 ** (len(word) - 1 - i)
words.sort(reverse=True)
result = 0
idx = 0
for num in range(9, -1, -1):
    if not words[idx]:
        break
    result += num * words[idx]
    idx += 1
print(result)