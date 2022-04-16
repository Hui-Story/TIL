w, h = map(int, input().split())

MAP = [[[0, 0, 0, 0] for _ in range(w)] for _ in range(h)]
MAP[0][1][1] = 1
MAP[1][0][0] = 1

for i in range(h):
    for j in range(w):
        a, b, c, d = MAP[i][j]
        if i + 1 < h:
            MAP[i + 1][j][0] += a + c
            MAP[i + 1][j][2] += b
        if j + 1 < w:
            MAP[i][j + 1][1] += b + d
            MAP[i][j + 1][3] += a

print(sum(MAP[h - 1][w - 1]) % 100000)