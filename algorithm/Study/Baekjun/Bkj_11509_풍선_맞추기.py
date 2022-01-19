N = int(input())

result = 0
arrows = [0] * 1000001
for i in map(int, input().split()):
    if not arrows[i]:
        result += 1
    else:
        arrows[i] -= 1
    arrows[i - 1] += 1

print(result)