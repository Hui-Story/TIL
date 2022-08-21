import sys

input = sys.stdin.readline

N: int = int(input())
name: list[str] = list(input().rstrip())
name_length: int = len(name)

for _ in range(N - 1):
    current_name: str = input().rstrip()
    for i in range(name_length):
        if name[i] != current_name[i]:
            name[i] = '?'

print(''.join(name))