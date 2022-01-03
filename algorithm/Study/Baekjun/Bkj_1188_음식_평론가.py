N, M = map(int, input().split())

from math import gcd

N = N % M
if not N:
    print(0)
else:
    print(M - gcd(N, M))


# result = 0

# while True:
#     N = N % M
#     if not N:
#         break
#     if M % N:
#         result += N
#         M = M - N
#     else:
#         result += (M - N)
#         break

# print(result)