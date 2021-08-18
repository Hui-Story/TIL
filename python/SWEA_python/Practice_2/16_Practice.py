N, M = map(int, input().split(','))

lst = [[0]*M for _ in range(N)]

for i in range(N):
    for j in range(M):
        lst[i][j] = i*j

print(lst)