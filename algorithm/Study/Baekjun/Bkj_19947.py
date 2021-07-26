H, Y = input().split()
H = int(H)
Y = int(Y)

dp = [0] * (Y+1)

for i in range(Y+1):
    if i == 0:
        dp[i] = H
    elif i >= 5:
        dp[i] = int(max(dp[i-1]*1.05, dp[i-3]*1.20, dp[i-5]*1.35))
    elif i >= 3:
        dp[i] = int(max(dp[i-1]*1.05, dp[i-3]*1.20))
    else:
        dp[i] = int(dp[i-1]*1.05)

print(int(dp[Y]))