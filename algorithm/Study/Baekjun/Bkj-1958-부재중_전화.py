N, L, D = map(int, input().split())

check = [True] * ((L + 5) * N)

idx = 0
for _ in range(N):
    for _ in range(L):
        check[idx] = False
        idx += 1
    idx += 5

time = 0
while True:
    if time >= (L + 5) * N or check[time]:
        print(time)
        break
    time += D