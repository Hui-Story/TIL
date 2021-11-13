import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    R, S = map(str, input().strip().split())
    R = int(R)
    result = ''
    for word in S:
        # 각 문자를 R 만큼 반복해서 결과에 추가
        result += word * R
    print(result)