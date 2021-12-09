def self_number(n):
    dn = n
    for i in str(n):
        dn += int(i)
    if dn < 10000:
        num_check[dn] = 0
        self_number(dn)

num_check = [1]*10000
for n in range(1, 10000):
    if num_check[n]:
        self_number(n)

for n in range(1, 10000):
    if num_check[n]:
        print(n)