import sys
input = sys.stdin.readline

def star(N):
    if N == 0:
        return ['*']
    else:
        result = star(N-1)
        # 이전 리스트를 순회하며 구현되는 별을 리스트에 추가
        for i in star(N-1):
            result.append(i+' '*(2**(N-1)-len(i))+i)
        return result

N = int(input())

star_result = star(N)
star_result.reverse()  # 역순으로 출력
print('\n'.join(star_result))