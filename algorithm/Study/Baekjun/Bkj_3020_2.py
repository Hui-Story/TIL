import sys

def binary(lst, start, end, key):
    global result
    while start <= end:
        middle = (start + end) // 2

        if lst[middle] >= key:
            end = middle - 1
        else:
            start = middle + 1
    return start

N, H = map(int, sys.stdin.readline().split())

lst1 = []
lst2 = []

for i in range(N//2):
    lst1.append(int(sys.stdin.readline()))
    lst2.append(H - int(sys.stdin.readline()))

lst1.sort()  # 석순
lst2.sort()  # 종유석

min_result = 2e+10
cnt = 1

for course in range(1, H + 1):

    result = 0

    result += (N//2 - binary(lst1, 0, (N//2)-1, course))
    result += binary(lst2, 0, (N//2)-1, course)

    if result <= min_result:
        if result == min_result:
            cnt += 1
        else:
            min_result = result
            cnt = 1

print(min_result, cnt)