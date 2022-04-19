S = input()

base = [0, 0, 0]
for i in S:
    base[ord(i) - 65] += 1

dp = [[] for _ in range(len(S))]
result = [''] * len(S)

for i in range(3):
    if base[i]:
        init = [base[0], base[1], base[2], i, 0, -1]
        init[i] -= 1
        dp[0].append(init)