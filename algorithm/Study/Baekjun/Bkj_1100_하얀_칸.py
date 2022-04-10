import sys
input = sys.stdin.readline

MAP = [str(input().strip()) for _ in range(8)]
result = 0

for i in range(8):
    for j in range(8):
        if (i + j) % 2 == 0:
            if MAP[i][j] == 'F':
                result += 1

print(result)