N = int(input())

A = list(map(int, input().split()))
result = 2000000000

s, e = 0, N-1
while s < e:
    temp = A[s] + A[e]
    if abs(temp) < abs(result):
        result = temp
        rs, re = A[s], A[e]
    if temp < 0:
        s += 1
    elif temp > 0:
        e -= 1
    else:
        break

print(rs, re)