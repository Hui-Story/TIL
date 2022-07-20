N = input()

answer = 'NO'

for i in range(1, len(N)):
    l = r = 1
    for num in N[:i]:
        l *= int(num)
    for num in N[i:]:
        r *= int(num)
    if l == r:
        answer = 'YES'

print(answer)