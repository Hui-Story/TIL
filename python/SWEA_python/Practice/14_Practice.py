a = int(input())
b = 0

for i in range(1, a+1):
    if a % i == 0:
        print('{0}(은)는 {1}의 약수입니다.'.format(i, a))
        b += 1
    if (a == i) & (b == 2):
        print('{1}(은)는 {0}과 {1}로만 나눌 수 있는 소수입니다.'.format(1, a))