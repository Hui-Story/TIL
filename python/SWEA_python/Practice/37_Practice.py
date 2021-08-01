n = int(input())

def fibo(n):
    if n == 0 or n == 1:
        return n
    else:
        return fibo(n-2) + fibo(n-1)

result = []
for i in range(1, n+1):
    result.append(fibo(i))

print(result)