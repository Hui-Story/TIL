for case in range(1, 11):
    dump = int(input())
    block = list(map(int, input().split()))
    for i in range(dump):
        max_num = 0
        max_idx = 0
        min_num = 2e+10
        min_idx = 0
        for idx in range(len(block)):
            if block[idx] > max_num:
                max_num = block[idx]
                max_idx = idx
            if block[idx] < min_num:
                min_num = block[idx]
                min_idx = idx
        if (max_num - min_num) <= 1:
            print(f'#{case} {max_num - min_num}')
            break
        else:
            block[max_idx] -= 1
            block[min_idx] += 1
    else:
        max_num = 0
        min_num = 2e+10
        for idx in range(len(block)):
            if block[idx] > max_num:
                max_num = block[idx]
            if block[idx] < min_num:
                min_num = block[idx]
        print(f'#{case} {max_num - min_num}')