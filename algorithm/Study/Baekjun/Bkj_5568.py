n = int(input())
k = int(input())
numbers = list(input() for _ in range(n))
numbers_2 = []
num = ''

for a in range(0, n):
    for b in range(0, n):
        if a == b:
            continue
        if k >= 3:
            for c in range(0, n):
                if (a == c) or (b == c):
                    continue 
                if k >= 4:
                    for d in range(0, n):
                        if (a == d) or (b == d) or (c == d):
                            continue
                        else:
                            num = str(numbers[a]) + str(numbers[b]) + str(numbers[c])+ str(numbers[d])
                            if num not in numbers_2:
                                numbers_2.append(num)
                                num = ''
                else:
                    num = str(numbers[a]) + str(numbers[b]) + str(numbers[c])
                    if num not in numbers_2:
                        numbers_2.append(num)
                        num = ''
        else:
            num = str(numbers[a]) + str(numbers[b])
            if num not in numbers_2:
                numbers_2.append(num)
                num = ''

print(len(numbers_2))