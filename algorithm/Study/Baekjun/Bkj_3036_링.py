
def gcd(x, y):
    while y:
        x, y = y, x % y
    return x

N = int(input())
rings = list(map(int, input().split()))

for i in range(1, N):
    g = gcd(rings[0], rings[i])
    print(f'{rings[0] // g}/{rings[i] // g}')