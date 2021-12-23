import sys
input = sys.stdin.readline

N = int(input())
result = 0
for _ in range(N):
    word = str(input().strip())
    check = [0] * 26
    for i in range(1, len(word)):
        if word[i] != word[i-1]:
            pre = ord(word[i-1]) - 97
            now = ord(word[i]) - 97
            check[pre] = 1
            if check[now]:
                break
    else:
        result += 1

print(result)