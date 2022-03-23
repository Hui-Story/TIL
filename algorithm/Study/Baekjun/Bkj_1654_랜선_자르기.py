import sys
input = sys.stdin.readline

K, N = map(int, input().split())
cables = [int(input()) for _ in range(K)]

s, e = 0, 2 ** 31
while s <= e:
    mid = (s + e) // 2
    cable_cnt = 0
    for cable in cables:
        cable_cnt += cable // mid
    if cable_cnt >= N:
        s = mid + 1
    else:
        e = mid - 1

print(e)