N = str(input())

nums = sorted([int(i) for i in N], reverse=True)

for num in nums:
    print(num, end='')