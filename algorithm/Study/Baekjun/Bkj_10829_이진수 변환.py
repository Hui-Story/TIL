N = int(input())

def binary(N):
    if N == 0:
        return '0'
    elif N == 1:
        return '1'
    # 2 로 나눈 나머지가 없는 경우
    if (N % 2 == 0):
        return binary(N/2) + '0'
    elif (N % 2 == 1):
        return binary((N-1)/2) + '1'

binary_N = binary(N)
print(binary_N)