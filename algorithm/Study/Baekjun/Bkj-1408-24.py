import sys

input = sys.stdin.readline

h1, m1, s1 = map(int, input().strip().split(':'))
h2, m2, s2 = map(int, input().strip().split(':'))

diff = (h2 - h1) * 3600 + (m2 - m1) * 60 + (s2 - s1)

if diff < 0:
    diff += 60 * 60 * 24

h3, m3, s3 = diff // 3600, (diff % 3600) // 60, diff % 60

print(str(h3).zfill(2) + ':' + str(m3).zfill(2) + ':' + str(s3).zfill(2))