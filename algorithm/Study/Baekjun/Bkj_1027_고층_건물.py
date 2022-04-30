N = int(input())
buildings = list(map(int, input().split()))
view_cnt = [0] * N

for l in range(N - 1):
    for r in range(l + 1, N):
        for n in range(l + 1, r):
            min_slope = (buildings[r] - buildings[l]) / (r - l)
            now_slope = (buildings[n] - buildings[l]) / (n - l)
            if now_slope >= min_slope:
                break
        else:
            view_cnt[l] += 1
            view_cnt[r] += 1

print(max(view_cnt))