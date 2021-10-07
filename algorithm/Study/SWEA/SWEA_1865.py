
def search(i, cnt):
    global result
    if cnt <= result:
        return
    if i == N:
        result = max(result, cnt)
        return
    for j in range(N):
        if not made[j]:
            made[j] = 1
            search(i+1, cnt * (success[i][j] / 100))
            made[j] = 0


T = int(input())

for case in range(1, T+1):
    N = int(input())
    success = [list(map(int, input().split())) for _ in range(N)]
    made = [0] * N
    result = 0

    search(0, 1)

    print('#{} {:.6f}'.format(case, result*100))