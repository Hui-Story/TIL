N = 1000 - int(input())

count = 0
while N:
    if N >= 500:
        N -= 500
    elif N >= 100:
        N -= 100
    elif N >= 50:
        N -= 50
    elif N >= 10:
        N -= 10
    elif N >= 5:
        N -= 5
    elif N >= 1:
        N -= 1
    count += 1

print(count)