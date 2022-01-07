from itertools import accumulate

def binary_search(num):
    global result
    s, e = 0, N-1
    while s <= e:
        m = (s + e) // 2
        if K_lst[m] < num:
            s = m + 1
        elif K_lst[m] > num:
            e = m - 1
        else:
            result += 1
            # for i in range(m-1, -1, -1):
            #     if K_lst[i] != num:
            #         break
            #     result += 1
            # for i in range(m+1, N):
            #     if K_lst[i] != num:
            #         break
            #     result += 1
            return

N, K = map(int, input().split())
A = list(accumulate(map(int, input().split())))
result = 0

K_lst = [K]
for i in range(N-1):
    K_lst.append(K + A[i])
K_lst.sort()

for num in A:
    binary_search(num)

print(result)