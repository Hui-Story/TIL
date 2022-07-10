X, Y = map(str, input().split())
X, Y = X[::-1], Y[::-1]

print(str(int(X) + int(Y))[::-1].lstrip('0'))