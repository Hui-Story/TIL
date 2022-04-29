N = int(input())
buildings = list(map(int, input().split()))
view_cnt = [0] * N

for l in range(N - 1):
    for r in range(l + 1, N):
        for n in range(l + 1, r):
            limit = (buildings[r] - buildings[l]) * ((n - l) / (r - l)) + buildings[l]
            print(limit)
            if buildings[n] >= limit:
                break
        else:
            view_cnt[l] += 1
            view_cnt[r] += 1

print(*view_cnt)
print(max(view_cnt))