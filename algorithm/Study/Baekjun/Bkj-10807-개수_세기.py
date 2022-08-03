import sys

input = sys.stdin.readline

N = int(input())
array = list(map(int, input().split()))
target = int(input())
answer = 0

for n in array:
    if n == target:
        answer += 1

print(answer)