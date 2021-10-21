import sys
input = sys.stdin.readline

N = int(input())
cycle = 1
num = N

while True:
    tmp = (num // 10) + (num % 10)
    num = (num % 10) * 10 + (tmp % 10)
    if num == N:
        break
    cycle += 1

print(cycle)