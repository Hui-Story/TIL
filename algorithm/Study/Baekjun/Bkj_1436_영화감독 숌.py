N = int(input())

a = 0
b = 0
while True:
    a += 1
    # '666'이 포함되어 있는 수를 b 로 카운트
    if '666' in str(a):
        b += 1
    if b == N:
        print(a)
        break