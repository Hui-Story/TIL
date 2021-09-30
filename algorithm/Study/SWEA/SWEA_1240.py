T = int(input())

def scan():
    arr = [0]*8
    codes = [str(input())[::-1] for _ in range(N)]
    result = 0
    for code in codes:
        if '1' not in code:
            continue
        for i in range(len(code)):
            if code[i] == '1':
                password = code[i:i+56][::-1]
                for j in range(8):
                    try:
                        arr[j] += pass_dic[password[j*7:j*7+7]]
                    except:
                        print('#{} 0'.format(case))
                        return
                for idx in range(8):
                    if idx % 2:
                        result += arr[idx]
                    else:
                        result += arr[idx]*3
                if result % 10:
                    print('#{} 0'.format(case))
                else:
                    print('#{} {}'.format(case, sum(arr)))
                return

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
    N, M = map(int, input().split())
    scan()