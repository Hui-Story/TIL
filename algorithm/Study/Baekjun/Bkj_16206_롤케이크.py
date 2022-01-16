N, M = map(int, input().split())
A = list(map(int, input().split()))
not_mod_ten = []
others = []

result = 0

for cake in A:
    if cake % 10:
        others.append(cake)
    else:
        if cake == 10:
            result += 1
        else:
            not_mod_ten.append(cake)
not_mod_ten.sort()

for cake in not_mod_ten:
    if M:
        cut = (cake // 10) - 1
        if M >= cut:
            M -= cut
            result += (cut + 1)
        else:
            result += M
            M = 0
            break
    else:
        break

for cake in others:
    if M:
        cut = cake // 10
        if M >= cut:
            M -= cut
            result += cut
        else:
            result += M
            M = 0
            break
    else:
        break

print(result)