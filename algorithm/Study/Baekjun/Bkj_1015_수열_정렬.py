N = int(input())
nums = list(map(int, input().split()))

sorted_nums = sorted(nums)
result = []
for i in range(N):
    idx = sorted_nums.index(nums[i])
    result.append(idx)
    sorted_nums[idx] -= 1

print(*result)