
def tower(i, now):
    global result
    if now >= B:
        result = min(result, now - B)
        return
    if i >= N:
        return
    tower(i+1, now + H[i])
    tower(i+1, now)

T = int(input())

for case in range(1, T+1):
    N, B = map(int, input().split())
    H = list(map(int, input().split()))
    result = 2e+10

    tower(0, 0)

    print('#{} {}'.format(case, result))