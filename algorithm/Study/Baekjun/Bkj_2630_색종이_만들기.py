import sys
input = sys.stdin.readline

def cut(x, y, n):
    if n == 1:
        result[paper[x][y]] += 1
    else:
        temp = paper[x][y]
        for dx in range(n):
            for dy in range(n):
                if paper[x + dx][y + dy] != temp:
                    cut(x, y, n // 2)
                    cut(x + n // 2, y, n // 2)
                    cut(x, y + n // 2, n // 2)
                    cut(x + n // 2, y + n // 2, n // 2)
                    return
        result[temp] += 1

N = int(input())
paper = [list(map(int, input().split())) for _ in range(N)]
result = [0, 0]

cut(0, 0, N)

print(result[0])
print(result[1])