import sys
input = sys.stdin.readline

number_cnt = [0]*42

for _ in range(10):
    num = int(input())
    number_cnt[num % 42] = 1

print(sum(number_cnt))