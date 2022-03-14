import sys
input = sys.stdin.readline

R, C = map(int, input().split())
vertical_words = [''] * C
for _ in range(R):
    word = input().strip()
    for i in range(C):
        vertical_words[i] = word[i] + vertical_words[i]
vertical_words.sort()
count = 0

start, end = 0, R

while True:
    if start >= end:
        print(start - 1)
        break
    mid = (start + end) // 2
    same_check = False
    for i in range(1, C):
        if vertical_words[i][:R - mid] == vertical_words[i - 1][:R - mid]:
            same_check = True
            break
    if same_check:
        end = mid
    else:
        start = mid + 1