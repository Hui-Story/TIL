import sys
input = sys.stdin.readline

N = int(input())
crane_loads = sorted(list(map(int, input().split())), reverse=True)
crane_cnt = [0] * N
max_cnt = 0
M = int(input())
boxs = sorted(list(map(int, input().split())), reverse=True)

if max(boxs) > max(crane_loads):
    print(-1)
    exit()

for box_idx in range(M):
    box = boxs[box_idx]
    for crane_idx in range(N):
        crane_load = crane_loads[crane_idx]
        if (box <= crane_load) and (crane_cnt[crane_idx] < max_cnt):
            crane_cnt[crane_idx] += 1
            max_cnt = max(max_cnt, crane_cnt[crane_idx])
            break
    else:
        crane_cnt[0] += 1
        max_cnt = max(max_cnt, crane_cnt[0])

print(max_cnt)