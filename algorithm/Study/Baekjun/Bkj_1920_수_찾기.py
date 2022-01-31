N = int(input())
A = list(map(int, input().split()))
A.sort()

M = int(input())
nums = list(map(int, input().split()))
sorted_nums = []
for i in range(M):
    sorted_nums.append((nums[i], i))
sorted_nums.sort()
result = [0] * M

i = j = 0
while i < N and j < M:
    num, idx = sorted_nums[j]
    if A[i] > num:
        j += 1
    elif A[i] < num:
        i += 1
    else:
        result[idx] = 1
        j += 1

for i in result:
    print(i)