a = int(input())

for i in range(1, a+1):
    if a % i == 0:
        print('{0}(은)는 {1}의 약수입니다.'.format(i, a))