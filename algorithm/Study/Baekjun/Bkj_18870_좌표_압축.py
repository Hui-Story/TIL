N = int(input())
nums = list(map(int, input().split()))
nums_lst = [[i, nums[i], 0] for i in range(N)]
nums_lst.sort(key=lambda x : x[1])

for i in range(1, N):
    if nums_lst[i][1] > nums_lst[i - 1][1]:
        nums_lst[i][2] = nums_lst[i - 1][2] + 1
    else:
        nums_lst[i][2] = nums_lst[i - 1][2]

nums_lst.sort(key=lambda x : x[0])
for idx, num, cnt in nums_lst:
    print(str(cnt), end=' ')