import sys

input = sys.stdin.readline

a = input().strip()
b = input().strip()

if len(a) >= len(b):
    print('go')
else:
    print('no')