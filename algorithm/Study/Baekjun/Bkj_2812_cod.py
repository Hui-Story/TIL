import sys
input = sys.stdin.readline

N, K = map(int, input().split())
number = str(input().strip())
result = ''

now_idx = 0
while K:
    max_num = -1
    max_idx = 0
    for i in range(K+1):
        if int(number[now_idx+i]) > max_num:
            max_num = int(number[now_idx+i])
            max_idx = now_idx+i
    result += number[max_idx]
    K -= (max_idx - now_idx)
    now_idx = (max_idx + 1)
    if len(result) == (N-K):
        now_idx = N
        break
result += number[now_idx:]

print(result)