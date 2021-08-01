scores = [85, 65, 77, 83, 75, 22, 98, 88, 38, 100]

i = len(scores) - 1
high_score = 0

while i >= 0:
    if scores[i] >= 80:
        high_score += scores.pop(i)
    i -= 1

print(high_score)