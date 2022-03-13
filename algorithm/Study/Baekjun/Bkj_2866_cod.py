import sys
input = sys.stdin.readline

R, C = map(int, input().split())
words = [input().strip() for _ in range(R)]
same_word_check = [[1] * C for _ in range(R)]
count = 0

for i in range(R - 1, -1, -1):
    if i == R - 1:
        for j in range(1, C):
            if words[i][j] == words[i][j - 1]:
                same_word_check[i][j] = same_word_check[i][j - 1]
            else:
                same_word_check[i][j] = same_word_check[i][j - 1] + 1
    else:
        for j in range(C):
            if same_word_check[i - 1][j] == same_word_check[i - 1][j - 1]:
                if words[i][j] == words[i][j - 1]:
                    same_word_check[i][j] = same_word_check[i][j - 1]
                else:
                    same_word_check[i][j] = same_word_check[i][j - 1] + 1
            else:
                same_word_check[i][j] = same_word_check[i][j - 1] + 1
    if same_word_check[i][-1] == R:
        pass