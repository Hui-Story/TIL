import sys

input = sys.stdin.readline

string1: str = input().strip()
string2: str = input().strip()
length1: int = len(string1)
length2: int = len(string2)
lcs: list[int] = [0] * max(length1, length2)

for i in range(length1):
    cnt: int = 0
    for j in range(length2):
        if cnt < lcs[j]:
            cnt = lcs[j]
        elif string1[i] == string2[j]:
            lcs[j] = cnt + 1

print(max(lcs))