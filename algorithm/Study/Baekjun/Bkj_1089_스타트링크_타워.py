import sys
input = sys.stdin.readline

# 가능한 숫자 체크
def num_check(i, num):
    global temp
    for x in range(5):
        for y in range(3):
            # 숫자에 해당하지 않는 전구가 켜져있는 경우
            if number_reference[x][num * 4 + y] == '.' and bulbs[x][i * 4 + y] == '#':
                return False
    temp += num
    return True


N = int(input())
bulbs = [input().strip() for _ in range(5)]
number_reference = [
    '###...#.###.###.#.#.###.###.###.###.###',
    '#.#...#...#...#.#.#.#...#.....#.#.#.#.#',
    '#.#...#.###.###.###.###.###...#.###.###',
    '#.#...#.#.....#...#...#.#.#...#.#.#...#',
    '###...#.###.###...#.###.###...#.###.###'
]

result = 0

# 각 자릿수 안내판
for i in range(N):
    num_cnt = 0
    temp = 0
    # 0 ~ 9 숫자
    for num in range(10):
        if num_check(i, num):
            num_cnt += 1
    # 가능한 숫자가 없는 경우
    if not num_cnt:
        print(-1)
        exit()
    # 가능한 숫자의 평균 합산
    result += (temp * (10 ** (N - i - 1))) / num_cnt

print(result)