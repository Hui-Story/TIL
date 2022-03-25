
def factorial(n):
    if n <= 1:
        return 1
    else:
        return n * factorial(n - 1)

n, m = map(int, input().split())

print(int(factorial(n) // (factorial(m) * factorial(n - m))))
