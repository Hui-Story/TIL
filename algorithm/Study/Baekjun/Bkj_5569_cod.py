w, h = map(int, input().split())

MAP = [[[0, 0] for _ in range(w)] for _ in range(h)]
MAP[0][1][1] = 1
MAP[1][0][0] = 1

for i in range(h):
    for j in range(w):
        if i + 1 < h:
            MAP[i + 1][j][0] += MAP[i][j][0]
        if i + 1 < h:
            MAP[i + 1][j][0] += MAP[i][j - 1][1]
        if j + 1 < w:
            MAP[i][j + 1][1] += MAP[i][j][1]
        if j + 1 < w:
            MAP[i][j + 1][1] += MAP[i - 1][j][0]

for i in MAP:
    print(i)
print(sum(MAP[h - 1][w - 1]))