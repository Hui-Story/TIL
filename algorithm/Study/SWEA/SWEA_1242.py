T = int(input().rstrip())

def scan():
    global result
    for i in range(N):
        j = M*4 - 1
        while j >= 0:
            if bit_MAP[i][j] == '1':
                if (i == 0) or (bit_MAP[i-1][j] != '1'):
                    arr = [0] * 8
                    check = 0
                    weight = 1
                    while True:
                        for k in range(8):
                            if bit_MAP[i][j-weight*7*(k+1)+1 : j-weight*7*k+1 : weight] in pass_dic.keys():
                                continue
                            else:
                                break
                        else:
                            break
                        weight += 1
                    for k in range(8):
                        arr[7-k] = pass_dic[bit_MAP[i][j-weight*7*(k+1)+1 : j-weight*7*k+1 : weight]]
                    for idx in range(8):
                        if idx % 2:
                            check += arr[idx]
                        else:
                            check += arr[idx]*3
                    if check % 10:
                        pass
                    else:
                        result += sum(arr)
                    j -= 56*weight
                else:
                    j -= 1
            else:
                j -= 1


pass_dic = {
    '0001101': 0,
    '0011001': 1,
    '0010011': 2,
    '0111101': 3,
    '0100011': 4,
    '0110001': 5,
    '0101111': 6,
    '0111011': 7,
    '0110111': 8,
    '0001011': 9,
}

for case in range(1, T+1):
    N, M = map(int, input().strip().split())
    MAP = [str(input().rstrip()) for _ in range(N)]
    bit_MAP = ['' for _ in range(N)]
    for i in range(N):
        for j in MAP[i]:
            bit_MAP[i] += bin(int(j, 16))[2:].zfill(4)

    result = 0
    scan()

    print(f'#{case} {result}')