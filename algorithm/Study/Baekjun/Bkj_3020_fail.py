import sys

N, H = map(int, sys.stdin.readline().split())

# 계차수열

lst1 = [0] * (N//2)
lst2 = [0] * (N//2)
lst1_in = []
lst2_in = []

for _ in range(N // 2):
    lst1_in.append(int(sys.stdin.readline()))
    lst2_in.append(H - int(sys.stdin.readline()))

cnt1 = [0] * (H + 1)
cnt2 = [0] * (H + 1)

for i in range(N // 2):
    cnt1[lst1_in[i]] += 1
    cnt2[lst2_in[i]] += 1

for i in range(1, H + 1):
    cnt1[i] += cnt1[i - 1]
    cnt2[i] += cnt2[i - 1]

for i in range(N // 2):
    lst1[cnt1[lst1_in[i]] - 1] = lst1_in[i]
    lst2[cnt2[lst2_in[i]] - 1] = lst2_in[i]
    cnt1[lst1_in[i]] -= 1
    cnt2[lst2_in[i]] -= 1

min_result = 2e+10
cnt = 1

for course in range(1, H + 1):

    result = 0

    low = 0
    high = (N // 2) - 1

    while low <= high:
        middle = (low + high) // 2

        if lst1[middle] >= course:
            high = middle - 1
        else:
            low = middle + 1

    result += (N // 2 - low)

    low = 0
    high = (N // 2) - 1

    while low <= high:
        middle = (low + high) // 2

        if lst2[middle] >= course:
            high = middle - 1
        else:
            low = middle + 1
    
    result += low

    if result <= min_result:
        if result == min_result:
            cnt += 1
        else:
            min_result = result
            cnt = 1

print(min_result, cnt)