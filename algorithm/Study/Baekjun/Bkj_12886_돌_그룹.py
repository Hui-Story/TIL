from collections import deque

def change(a, b):
    if a > b:
        return (a - b, 2 * b)
    elif a < b:
        return (2 * a, b - a)
    else:
        return False

A, B, C = map(int, input().split())
S = A + B + C

dp = [[0] * (S + 1) for _ in range(S + 1)]
deq = deque()
deq.append((A, B))
dp[A][B] = 1

while deq:
    a, b = deq.popleft()
    c = S - a - b
    if a == b == c:
        print(1)
        exit()
    for sa, sb in [(a, b), (a, c), (b, c)]:
        result = change(sa, sb)
        if result:
            na, nb = result
            nc = S - na - nb
            min_cnt, max_cnt = min(na, nb, nc), max(na, nb, nc)
            if not dp[min_cnt][max_cnt]:
                deq.append((min_cnt, max_cnt))
                dp[min_cnt][max_cnt] = 1

print(0)