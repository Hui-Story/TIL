N = int(input())

def star(N):
    star_2 = []
    if N == 0:
        return ['*']
    else:
        for i in range(2**(N-1)):
            star_2 = star_2 + [star(N-1)[i] + ' '*(2**(N-1)-i-1) + star(N-1)[i]]
        return star(N-1) + star_2

for i in range(len(star(N))):
    print(star(N)[len(star(N))-i-1])