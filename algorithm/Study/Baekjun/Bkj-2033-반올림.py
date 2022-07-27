N = int(input())
i = 10

while N > i:
    if N % i >= i // 2:
        N += i
    N -= (N % i)
    i *= 10

print(N)