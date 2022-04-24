N = int(input())
P = list(map(int, input().split()))
M = int(input())
sorted_price = sorted([(P[num], num) for num in range(N)], key=lambda x: (x[0], -x[1]))
result = []

if N == 1 or min(P[1:]) > M:
    print(0)
    exit()

for price, num in sorted_price:
    if price <= M and num != 0:
        result.append((price, num))
        M -= price
        break

min_price, max_num = sorted_price[0]
while True:
    if M < min_price:
        break
    result.append((min_price, max_num))
    M -= min_price

for i in range(len(result)):
    now_price, now_num = result[i]
    for j in range(N - 1, -1, -1):
        price = P[j]
        if now_price + M >= price and now_num < j:
            result[i] = (price, j)
            M -= (price - now_price)
            break
    else:
        if i >= 1:
            break

for price, num in result:
    print(str(num), end='')