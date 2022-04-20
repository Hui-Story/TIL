
def record(a, b, c, d, e, i):
    global dp, result
    if a == 0 and b == 0 and c == 0:
        return True
    if dp[a][b][c][d][e]:
        return False
    dp[a][b][c][d][e] = True
    result[i] = 'A'
    if a and record(a - 1, b, c, 0, d, i + 1):
        return True
    if b and d != 1:
        result[i] = 'B'
        if record(a, b - 1, c, 1, d, i + 1):
            return True
    if c and d != 2 and e != 2:
        result[i] = 'C'
        if record(a, b, c - 1, 2, d, i + 1):
            return True
    return False

S = input()

base = [0, 0, 0]
for i in S:
    base[ord(i) - 65] += 1

dp = [[[[[0] * 3 for _ in range(3)] for _ in range(51)] for _ in range(51)] for _ in range(51)]
result = [''] * len(S)

if record(*base, 0, 0, 0):
    print(''.join(result))
else:
    print(-1)