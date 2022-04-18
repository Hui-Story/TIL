n = int(input())
nums = sorted(list(map(int, input().split())))
x = int(input())
l, r = 0, n - 1
result = 0

while l < r:
    if nums[l] + nums[r] > x:
        r -= 1
    elif nums[l] + nums[r] < x:
        l += 1
    else:
        result += 1
        l, r = l + 1, r - 1

print(result)