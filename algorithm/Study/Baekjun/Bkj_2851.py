N = list(int(input()) for _ in range(10))

score = 0
for i in N:
    if abs(100-score) >= abs(100-(score+i)):
        score += i
    else:
        print(score)
        break
else:
    print(score)