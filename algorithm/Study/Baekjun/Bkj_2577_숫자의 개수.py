import sys
input = sys.stdin.readline

arr = [0]*10
num = 1
for _ in range(3):
    num *= int(input())

for i in str(num):
    arr[int(i)] += 1

for i in arr:
    print(i)