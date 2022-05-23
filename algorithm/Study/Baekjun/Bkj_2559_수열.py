import sys
input = sys.stdin.readline

N, K = map(int, input().split())
temp = list(map(int, input().split()))
now_sum = sum(temp[:K])
max_sum = now_sum

for i in range(N - K):
    now_sum += - temp[i] + temp[i + K]
    max_sum = max(max_sum, now_sum)

print(max_sum)