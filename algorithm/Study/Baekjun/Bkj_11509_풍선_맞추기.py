N = int(input())
H = list(map(int, input().split()))

result = 0
arrows = [0] * (N + 1)
for i in H:
    if not arrows[i]:
        result += 1
    else:
        arrows[i] -= 1
    arrows[i - 1] += 1

print(result)