def star(n):
    if n == 1:
        return ['*']
    now = []
    before = star(n - 1)
    now.append('*' + before[0] + '*' + before[0] + '*')
    for i in range(1, len(before) + 1):
        now.append('*' + ' ' * (len(before[0]) - i * 2 + 1) + before[-i] + ' ' * (len(before[0]) - i * 2 + 1) + '*')
    for i in range(1, len(before)):
        now.append('*' + ' ' * (len(before[0]) - i * 2) + '*')
    now.append('*')
    return now


N = int(input())

pattern = star(N)

if N % 2:
    for i in range(len(pattern) - 1, -1, -1):
        print(' ' * i + pattern[i])
else:
    for i in range(len(pattern)):
        print(' ' * i + pattern[i])
