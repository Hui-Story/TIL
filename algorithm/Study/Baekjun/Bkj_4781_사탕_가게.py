import sys
input = sys.stdin.readline

while True:
    n, m = map(float, input().split())
    if not n and not m:
        break
    n, m = int(n), int(m*100 + 0.5)
    dp = [0] * (m+1)
    
    for _ in range(1, n+1):
        c, p = map(float, input().split())
        c, p = int(c), int(p*100 + 0.5)
        for j in range(p, m + 1):
            dp[j] = max(dp[j-p] + c, dp[j])
    
    print(dp[m])