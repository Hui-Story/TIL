def check_m_o(n, k):
    if k and n <= moo_arr[k-1]:
        return check_m_o(n, k-1)
    if k:
        n -= moo_arr[k-1]
    if n <= k+3:
        if n == 1:
            return 'm'
        else:
            return 'o'
    else:
        n -= (k+3)
    return check_m_o(n, k-1)

N = int(input())

k = 0
moo_arr = [3]
while True:
    if k:
        moo_arr.append(moo_arr[k-1]*2 + k+3)
    if N <= moo_arr[k]:
        break
    k += 1

print(check_m_o(N, k))