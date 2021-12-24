import sys
input = sys.stdin.readline

while True:
    n, m = map(float, input().split())
    if not n and not m:
        break
    n, m = int(n), int(m*100)
    dp = [[0]*(m+1) for _ in range(n+1)]
    
    for i in range(1, n+1):
        c, p = map(float, input().split())
        c, p = int(c), int(p*100)
        for j in range(1, m+1):
            for k in range(1, (j // p) + 1):
                dp[i][j] = max(dp[i-1][j-(p * k)] + (c * k), dp[i-1][j], dp[i][j])
            dp[i][j] = max(dp[i-1][j], dp[i][j])
    
    print(max(dp[n]))