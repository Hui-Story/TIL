
def star(n):
    if n == 1:
        return ['*']
    else:
        pattern = []
        pre_pattern = star(n // 3)
        for i in pre_pattern:
            pattern.append(i * 3)
        for i in pre_pattern:
            pattern.append(i + ' ' * (n // 3) + i)
        for i in pre_pattern:
            pattern.append(i * 3)
        return pattern

N = int(input())

stars = star(N)

for i in stars:
    print(i)