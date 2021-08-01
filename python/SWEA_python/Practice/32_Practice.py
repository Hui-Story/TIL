n = int(input())

result = ''
while n >= 1:
    result = str(n % 2) + result
    n = n // 2

print(int(result))