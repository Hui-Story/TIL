import sys
input = sys.stdin.readline

def power(n):
    if n == 1:
        return matrix
    elif n == 2:
        return matrix_multiple(matrix, matrix)
    elif n % 2 == 0:
        arr = power(n//2)
        return matrix_multiple(arr, arr)
    else:
        arr = power(n//2)
        arr2 = matrix_multiple(arr, arr)
        return matrix_multiple(arr2, matrix)

def matrix_multiple(arr1, arr2):
    result = [[0]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            for k in range(N):
                result[i][j] += arr1[i][k]*arr2[k][j]
            result[i][j] = result[i][j] % 1000
    return result


N, B = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(N)]

result = power(B)

for i in range(N):
    for j in range(N):
        result[i][j] = result[i][j] % 1000

for i in result:
    print(*i)