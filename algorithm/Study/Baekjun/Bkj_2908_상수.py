A, B = map(str, input().split())

A_r = ''
B_r = ''

for i in range(3):
    A_r = A[i] + A_r
    B_r = B[i] + B_r

print(max(A_r, B_r))