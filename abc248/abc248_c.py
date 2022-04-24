mod = 998244353

n, m, k = map(int, input().split())

dp = [[0] * (k + 1) for _ in range(n + 1)]
dp[0][0] = 1

for i in range(1, n + 1):
    for j in range(1, k + 1):
        for z in range(1, m + 1):
            if j - z >= 0:
                dp[i][j] = (dp[i][j] + dp[i - 1][j - z]) % mod

ans = 0

for i in range(1, k + 1):
    ans = (ans + dp[n][i]) % mod

print(ans)