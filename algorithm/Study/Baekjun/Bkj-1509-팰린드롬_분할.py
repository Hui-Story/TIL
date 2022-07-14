
def is_palindrome(word):
    return word == word[::-1]

string = input()
length = len(string)
dp = [[5000] * length for _ in range(length)]
dp[0][0] = 1

for i in range(length):
    for j in range(i, length):
        if i == j and i:
            dp[i][j] = min(d[j - 1] for d in dp[:i]) + 1
            continue
        if is_palindrome(string[i:j + 1]):
            dp[i][j] = dp[i][i]

print(min(d[-1] for d in dp))