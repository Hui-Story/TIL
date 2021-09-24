N = int(input())
arr1 = list(map(int, input()))
arr2 = list(map(int, input()))

arr1_2 = list(arr1)
result = -1

cnt = 0

for i in range(N):
    if i == 0:
        cnt += 1
        for t in range(i, i+2):
            arr1[t] = 1 - arr1[t]
    else:
        if arr1[i-1] != arr2[i-1]:
            cnt += 1
            for t in range(i-1, min(i+2, N)):
                arr1[t] = 1 - arr1[t]

if arr1 == arr2:
    result = cnt

cnt = 0

for i in range(N):
    if i == 0:
        continue
    else:
        if arr1_2[i-1] != arr2[i-1]:
            cnt += 1
            for t in range(i-1, min(i+2, N)):
                arr1_2[t] = 1 - arr1_2[t]

if arr1_2 == arr2:
    if result != -1:
        result = min(result, cnt)
    else:
        result = cnt

print(result)