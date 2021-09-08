import sys
input = sys.stdin.readline

def star(N):
    if N == 0:
        return ['*']
    else:
        result = star(N-1)
        for i in star(N-1):
            result.append(i+' '*(2**(N-1)-len(i))+i)
        return result

N = int(input())

star_result = star(N)
star_result.reverse()
print('\n'.join(star_result))