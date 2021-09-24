import sys
input = sys.stdin.readline

N = int(input().strip())
meet = [list(map(int, input().strip().split())) for _ in range(N)]

meet = sorted(meet, key=lambda x : (x[1], x[0]))

cnt = 0
idx = 0
time = 0

while idx < N:
    if meet[idx][0] >= time:
        cnt += 1
        time = meet[idx][1]
    idx += 1

print(cnt)