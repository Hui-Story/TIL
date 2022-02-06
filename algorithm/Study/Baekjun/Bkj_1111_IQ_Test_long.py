N = int(input())
nums = list(map(int, input().split()))

if len(nums) == 1:
    print('A')
elif len(nums) == 2:
    if nums[0] == nums[1]:
        print(nums[0])
    else:
        print('A')
else:
    diff = []
    for i in range(N - 1):
        diff.append(nums[i + 1] - nums[i])
    if diff.count(0) == len(diff):
        print(nums[i])
        exit()
    pat = []
    for i in range(N - 2):
        if not diff[i + 1]:
            pat.append(0)
            continue
        if not diff[i] or diff[i + 1] % diff[i]:
            print('B')
            exit()
        pat.append(diff[i + 1] // diff[i])
    if pat.count(pat[0]) == len(pat):
        print(nums[-1] + (diff[-1] * pat[0]))
    else:
        print('B')