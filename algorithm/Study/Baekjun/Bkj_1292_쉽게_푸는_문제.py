A, B = map(int, input().split())
arr = []
num = 1
cnt = 0

while cnt < 1000:
    for _ in range(num):
        arr.append(num)
        cnt += 1
    num += 1

print(sum(arr[A - 1 : B]))