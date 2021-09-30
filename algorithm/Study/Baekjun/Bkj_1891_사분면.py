def find_loca(num, check):
    num = str(num)
    start = 0
    end = 2**(d)-1
    for i in range(d):
        if num[i] in check:
            end = (start+end) // 2
        else:
            start = (start+end) // 2 + 1
    return start

def find_num(i, j):
    result = ''
    mid_i = 2**(d) // 2
    mid_j = 2**(d) // 2
    for k in range(1, d+1):
        if i < (mid_i):
            if j < (mid_j):
                result += '2'
                mid_j -= 2**(d-k) // 2
            else:
                result += '1'
                mid_j += 2**(d-k) // 2
            mid_i -= 2**(d-k) // 2
        else:
            if j < (mid_j):
                result += '3'
                mid_j -= 2**(d-k) // 2
            else:
                result += '4'
                mid_j += 2**(d-k) // 2
            mid_i += 2**(d-k) // 2
    return result


d, number = map(int, input().split())
x, y = map(int, input().split())

i = find_loca(number, ['1', '2'])
j = find_loca(number, ['2', '3'])

i, j = i-y, j+x

if 0 <= i < 2**d and 0 <= j < 2**d:
    print(find_num(i, j))
else:
    print(-1)