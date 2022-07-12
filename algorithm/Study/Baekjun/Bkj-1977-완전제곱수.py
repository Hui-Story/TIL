M = int(input())
N = int(input())
nums = []
idx = 1

while idx ** 2 <= N:
    if M <= idx ** 2 <= N:
        nums.append(idx ** 2)
    idx += 1

if nums == []:
    print(-1)
else:
    print(sum(nums))
    print(nums[0])