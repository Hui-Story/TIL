
def power(a, b):
    if b == 1:
        return a % C
    else:
        temp = power(a, b // 2)
        if not b % 2:
            return (temp * temp) % C
        else:
            return (temp * temp * a) % C

A, B, C = map(int, input().split())

print(power(A, B))