import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    n = int(input())
    result = 1
    clothes_dic = dict()
    for _ in range(n):
        clothes, category = input().strip().split()
        if clothes_dic.get(category):
            clothes_dic[category] += 1
        else:
            clothes_dic[category] = 1
    
    for key, value in clothes_dic.items():
        result *= (value + 1)

    print(result - 1)