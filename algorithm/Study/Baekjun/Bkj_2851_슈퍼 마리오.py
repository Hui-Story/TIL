N = list(int(input()) for _ in range(10))

score = 0
for i in N:
    # 100 이후가 이전보다 100에 가까운 경우 합산 (같은 경우에도 합산)
    if abs(100-score) >= abs(100-(score+i)):
        score += i
    else:
        print(score)
        break
else:
    print(score)