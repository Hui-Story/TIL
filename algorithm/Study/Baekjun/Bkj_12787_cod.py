T = int(input())

for _ in range(T):
    M, N = map(str, input().split())
    
    if M == '1':
        cnt = 0
        num = ''
        result = 0
        for i in range(len(N)-1, -1, -1):
            if N[i] == '.':
                result += int(num)*(256**cnt)
                cnt += 1
                num = ''
            else:
                num = N[i] + num
        result += int(num)*(256**cnt)
        print(result)
    else:
        N = int(N)
        cnt = 1
        result = []
        while 256**cnt <= N:
            result.append(str((N % (256**cnt)) // (256**(cnt-1))))
            cnt += 1

        result.reverse()
        print('.'.join(result))