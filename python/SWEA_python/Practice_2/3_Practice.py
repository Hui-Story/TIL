lst = [(90, 80), (85, 75), (90, 100)]

for i in range(0, 3):
    print(f'{i+1}번 학생의 총점은 {sum(lst[i])}점이고, 평균은 {sum(lst[i])/2}입니다.')