N = int(input())
numbers = [0] * N
numbers[0] = 1
now_color = 2

for i in range(2, N+1):
    if numbers[i-1] == 0:
        for j in range(i, N+1, i):
            if numbers[j-1] == 0:
                numbers[j-1] = now_color
        now_color += 1

print(now_color-1)
print(*numbers)