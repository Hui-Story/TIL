N = int(input())
honeys = list(map(int, input().split()))
# 벌통이 중간에 있는 경우의 최대
result = sum(honeys[1:-1]) + max(honeys[1:-1])

# 벌통이 왼쪽에 있는 경우 최대 탐색
honey_cnt = sum(honeys[1:-1])
for i in range(1, N - 1):
    honey_cnt += (honeys[i - 1] * 2 - honeys[i])
    result = max(result, honey_cnt)

# 벌통이 오른쪽에 있는 경우 최대 탐색
honey_cnt = sum(honeys[1:-1])
for i in range(N - 2, 0, -1):
    honey_cnt += (honeys[i + 1] * 2 - honeys[i])
    result = max(result, honey_cnt)

print(result)