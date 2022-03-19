N = int(input())

for num in range(1, N + 1):
    cnt = num
    for i in str(num):
        cnt += int(i)
    if cnt == N:
        print(num)
        break
else:
    print(0)