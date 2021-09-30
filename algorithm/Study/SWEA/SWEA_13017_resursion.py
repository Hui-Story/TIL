T = int(input())

def change(idx):
    global bit, result
    if result != 'overflow':
        return

    now = 0
    for i in range(1, 13):
        if bit & (1 << (12-i)):
            now += 2**(-i)

    if N == now:
        result = bin(bit)[3:]
        return

    if idx >= 0:
        bit |= (1 << idx)
        change(idx-1)
        bit ^= (1 << idx)
        change(idx-1)
    return
    
    
for case in range(1, T+1):
    N = float(input())
    
    bit = 1 << 12
    result = 'overflow'

    change(11)

    print('#{} {}'.format(case, result.rstrip('0')))