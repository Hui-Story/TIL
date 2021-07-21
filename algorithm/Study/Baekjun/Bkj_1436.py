N = int(input())

a = 0
b = 0
while True:
    a += 1
    if '666' in str(a):
        b += 1
    if b == N:
        print(a)
        break