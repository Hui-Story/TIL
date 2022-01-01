import math

D, H, W = map(int, input().split())

temp = D / (math.sqrt(H**2 + W**2))

print(int(H * temp), int(W * temp))