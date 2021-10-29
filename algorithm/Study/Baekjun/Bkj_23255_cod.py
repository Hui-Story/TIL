import sys
input = sys.stdin.readline

N, M = map(int, input().split())
result = [1] * N
bridge_list = []

for _ in range(M):
    inp = list(map(int, input().split()))
    inp.sort()
    bridge_list.append(inp)

bridge_list.sort(key = lambda x : x[1])

for bridge in bridge_list:
    if result[bridge[0]-1] == result[bridge[1]-1]:
        result[bridge[1]-1] = result[bridge[0]-1] + 1

print(*result)