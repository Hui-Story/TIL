T = int(input())

for _ in range(T):
    M, N = map(str, input().split())
    
    if M == '1':
        result = 0
        p = 1
        nums = list(N.split('.'))
        for i in range(len(nums) - 1, - 1, - 1):
            result += int(nums[i]) * p
            p *= 256
        print(result)
    else:
        N = int(N)
        result = []
        p = 256 ** 7
        for _ in range(8):
            result.append(str(N // p))
            N %= p
            p //= 256
        print('.'.join(result))