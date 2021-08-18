import sys

N, H = map(int, sys.stdin.readline().split())

lst1 = []
lst2 = []

for i in range(N//2):
    lst1.append(int(sys.stdin.readline()))
    lst2.append(H - int(sys.stdin.readline()))

lst1.sort()  # 석순
lst2.sort()  # 종유석

# 계차수열

"""
lst1 = []
lst2 = []
lst1_in = []
lst2_in = []

for i in range(N//2):
    lst1_in.append(int(sys.stdin.readline()))
    lst2_in.append(H - int(sys.stdin.readline()))

lst1_count = [0] * (H+1)
lst2_count = [0] * (H+1)

for i in range(N//2):
    lst1_count[lst1_in[i]] += 1
    lst2_count[lst2_in[i]] += 1

for i in range(1, H+1):
    for j in range(lst1_count[i]):
        lst1.append(i)

for i in range(1, H+1):
    for j in range(lst2_count[i]):
        lst2.append(i)

"""

min_result = 2e+10
cnt = 1

for course in range(1, H+1):

    result = 0

    low = 0
    high = N//2

    while True:
        middle = (low + high) // 2

        if low == high:
            result += (N//2 - low)
            break
        elif lst1[middle] >= course:
            high = middle
        else:
            low = middle + 1
    
    low = 0
    high = N//2
    
    while True:
        middle = (low + high) // 2

        if low == high:
            result += low
            break
        elif lst2[middle] >= course:
            high = middle
        else:
            low = middle + 1
    
    if result <= min_result:
        if result == min_result:
            cnt += 1
        else:
            min_result = result
            cnt = 1

print(min_result, cnt)