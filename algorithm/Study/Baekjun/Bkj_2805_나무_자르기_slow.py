import sys
input = sys.stdin.readline

N, M = map(int, input().split())
trees = list(map(int, input().split()))

start, end = 0, max(trees)

while True:
    if start >= end:
        print(start - 1)
        break
    mid = (start + end) // 2
    total_tree = 0
    for tree in trees:
        if tree > mid:
            total_tree += (tree - mid)
    if total_tree >= M:
        start = mid + 1
    else:
        end = mid