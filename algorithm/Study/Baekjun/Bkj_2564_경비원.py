import sys
input = sys.stdin.readline

MIIS = lambda: map(int, input().split())

W, V = MIIS()
N = int(input())
shops = [tuple(MIIS()) for _ in range(N)]
sd, si = MIIS()

result = 0

for d, i in shops:
    temp = sd + d
    if sd == d:
        result += abs(si - i)
    elif temp == 3:
        result += min(si + i, (W - si) + (W - i)) + V
    elif temp == 7:
        result += min(si + i, (V - si) + (V - i)) + W
    elif temp == 4:
        result += si + i
    elif temp == 6:
        result += (W + V) - (si + i)
    elif sd == 1 and d == 4:
        result += (W - si) + i
    elif sd == 4 and d == 1:
        result += si + (W - i)
    elif sd == 2 and d == 3:
        result += si + (V - i)
    elif sd == 3 and d == 2:
        result += (V - si) + i

print(result)