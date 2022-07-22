import sys

input = sys.stdin.readline
LCS = list[list[int]]

def make_lcs_table(string1: str, string2: str, length1: int, length2: int) -> LCS:
    lcs: LCS = [[0] * (length1 + 1) for _ in range(length2 + 1)]

    for i in range(1, length2 + 1):
        for j in range(1, length1 + 1):
            if string2[i - 1] == string1[j - 1]:
                lcs[i][j] = lcs[i - 1][j - 1] + 1
            else:
                lcs[i][j] = max(lcs[i][j - 1], lcs[i - 1][j])

    return lcs

def search_lcs(lcs: LCS, string1: str, string2: str, length1: int, length2: int) -> str:
    i: int
    j: int
    i, j = length2, length1
    answer: str = ''

    while i and j:
        if string2[i - 1] == string1[j - 1]:
            answer = string2[i - 1] + answer
            i, j = i - 1, j - 1
        else:
            current_cnt: int = lcs[i][j]
            if lcs[i - 1][j] == current_cnt:
                i -= 1
            elif lcs[i][j - 1] == current_cnt:
                j -= 1

    return answer


string1: str = input().strip()
string2: str = input().strip()
length1: int = len(string1)
length2: int = len(string2)

lcs: LCS = make_lcs_table(string1, string2, length1, length2)
answer: str = search_lcs(lcs, string1, string2, length1, length2)
max_cnt: int = len(answer)

print(max_cnt)
if max_cnt:
    print(answer)