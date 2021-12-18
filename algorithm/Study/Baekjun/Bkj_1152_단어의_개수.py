words = str(input())

check = False
result = 0

for i in words:
    if i == ' ':
        check = False
    else:
        if not check:
            result += 1
        check = True

print(result)