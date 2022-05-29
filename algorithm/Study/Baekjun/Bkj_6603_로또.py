import sys, itertools
input = sys.stdin.readline

while True:
    nums = list(map(int, input().split()))
    if not nums[0]:
        break
    comb = itertools.combinations(nums[1:], 6)
    for c in comb:
        print(*c)
    print()