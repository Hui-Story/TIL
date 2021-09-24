N, M = map(int, input().split())
mat_1 = [list(map(int, input())) for _ in range(N)]
mat_2 = [list(map(int, input()))for _ in range(N)]

cnt = 0

for i in range(N-2):
    for j in range(M-2):
        if mat_2[i][j] != mat_1[i][j]:
            cnt += 1
            for di in range(3):
                for dj in range(3):
                    mat_2[i+di][j+dj] = 1 - mat_2[i+di][j+dj]

if mat_1 == mat_2:
    print(cnt)
else:
    print(-1)