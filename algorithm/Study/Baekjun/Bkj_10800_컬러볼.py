import sys
input = sys.stdin.readline

N = int(input())
balls = []
for i in range(N):
    C, S = map(int, input().split())
    balls.append((C, S, i))
balls.sort(key=lambda x : (x[1], x[0]))

colors = [0] * (N + 1)
color_cnt = balls[0][1]
total_size = 0
size_cnt = balls[0][1]
result = [0] * N

for i in range(1, N):
    C, S, num = balls[i]
    pC, pS, pnum = balls[i - 1]
    if S == pS:
        size_cnt += S
        if C == pC:
            color_cnt += S
        else:
            colors[pC] += color_cnt
            color_cnt = S
        result[num] = total_size - colors[C]
    else:
        total_size += size_cnt
        size_cnt = S
        colors[pC] += color_cnt
        color_cnt = S
        result[num] = total_size - colors[C]

for i in result:
    print(i)