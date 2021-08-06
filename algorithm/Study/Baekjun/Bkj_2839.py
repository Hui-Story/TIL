N = int(input())

total = N // 5
re_sugar = N % 5

if re_sugar % 3 == 0:
    total += re_sugar // 3
elif re_sugar == 1 and total >= 1:
    total += 1
elif re_sugar == 2 and total >= 2:
    total += 2
elif re_sugar == 4 and total >= 1:
    total += 2
else:
    total = -1

print(total)