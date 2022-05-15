import sys
input = sys.stdin.readline

W, H, X, Y, P = map(int, input().split())
result = 0
for _ in range(P):
    x, y = map(int, input().split())
    if Y <= y <= Y + H:
        if X <= x <= X + W:
            result += 1
        elif ((x - X) * (x - X) + (y - (Y + (H // 2))) * (y - (Y + (H // 2)))) <= (H // 2) * (H // 2):
            result += 1
        elif ((x - (X + W)) * (x - (X + W)) + (y - (Y + (H // 2))) * (y - (Y + (H // 2)))) <= (H // 2) * (H // 2):
            result += 1

print(result)