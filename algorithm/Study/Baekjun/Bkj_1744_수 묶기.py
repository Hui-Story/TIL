import sys
input = sys.stdin.readline

N = int(input())
numbers = [int(input()) for _ in range(N)]
numbers.sort()

result = 0

idx = 0

while idx < N:
    if numbers[idx] < 0:
        if idx+1 < N and numbers[idx+1] <= 0:
            result += numbers[idx]*numbers[idx+1]
            idx += 2
        else:
            result += numbers[idx]
            idx += 1
    elif numbers[idx] == 0 or numbers[idx] == 1:
        result += numbers[idx]
        idx += 1
    else:
        if (N-idx) % 2:
            result += numbers[idx]
            idx += 1
        else:
            result += numbers[idx]*numbers[idx+1]
            idx += 2

print(result)