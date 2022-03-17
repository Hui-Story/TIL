import sys
input = sys.stdin.readline

H, W = map(int, input().split())
blocks = list(map(int, input().split()))
total_rain = 0

if W <= 2:
    print(0)
    exit()

rain_cnt = 0
high_block = 0
for block in blocks:
    if block >= high_block:
        high_block = block
        total_rain += rain_cnt
        rain_cnt = 0
    else:
        rain_cnt += (high_block - block)

rain_cnt = 0
high_block = 0
for block in reversed(blocks):
    if block > high_block:
        high_block = block
        total_rain += rain_cnt
        rain_cnt = 0
    else:
        rain_cnt += (high_block - block)

print(total_rain)