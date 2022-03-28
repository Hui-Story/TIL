import sys, math
input = sys.stdin.readline

N = int(input())
crane_loads = sorted(list(map(int, input().split())), reverse=True)
M = int(input())
boxs = sorted(list(map(int, input().split())), reverse=True)

if max(boxs) > max(crane_loads):
    print(-1)
    exit()

time = 0
while M:
    time += 1
    crane_idx = 0
    for i in range(len(boxs)):
        if crane_idx >= N:
            break
        if boxs[i] and (boxs[i] <= crane_loads[crane_idx]):
            boxs[i] = 0
            crane_idx += 1
            M -= 1

print(time)