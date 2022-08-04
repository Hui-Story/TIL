import sys

input = sys.stdin.readline

array = [0] * 30

for _ in range(28):
    array[int(input()) - 1] = 1

for i in range(30):
    if array[i] == 0:
        print(i + 1)
        break

for i in range(29, -1, -1):
    if array[i] == 0:
        print(i + 1)
        break