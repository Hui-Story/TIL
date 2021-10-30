import sys
input = sys.stdin.readline

N, M = map(int, input().split())
result = [1] * N
bridge_list = [[] for _ in range(N)]
num_check = [[] for _ in range(N)]

for _ in range(M):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    if b < a:
        bridge_list[b].append(a)
    else:
        bridge_list[a].append(b)

for i in range(N):
    num = 1
    while True:
        if num not in num_check[i]:
            result[i] = num
            break
        num += 1
    for idx in bridge_list[i]:
        num_check[idx].append(result[i])

print(*result)