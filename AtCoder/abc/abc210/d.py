inf = 1 << 60
H, W, C = map(int, input().split())
G = []
dp = [[inf] * W for _ in range(H)]
X = [[inf] * W for _ in range(H)]
for _ in range(H):
    w = list(map(int, input().split()))
    G.append(w)
ans = inf
for i in range(H):
    for j in range(W):
        if i == 0 and j == 0:
            dp[i][j] = G[i][j]
            X[i][j] = inf
        elif i == 0:
            dp[i][j] = min(dp[i][j - 1] + C, G[i][j])
            X[i][j] = min(dp[i][j - 1] + C + G[i][j], X[i][j])
        elif j == 0:
            dp[i][j] = min(dp[i - 1][j] + C, G[i][j])
            X[i][j] = min(dp[i - 1][j] + C + G[i][j], X[i][j])
        else:
            dp[i][j] = min(dp[i - 1][j] + C, dp[i][j - 1] + C, G[i][j])
            X[i][j] = min(dp[i][j - 1] + C + G[i][j], dp[i - 1][j] + C + G[i][j], X[i][j])
            ans = min(ans, X[i][j])
G = G[::-1]
dp = [[inf] * W for _ in range(H)]
X = [[inf] * W for _ in range(H)]
for i in range(H):
    for j in range(W):
        if i == 0 and j == 0:
            dp[i][j] = G[i][j]
            X[i][j] = inf
        elif i == 0:
            dp[i][j] = min(dp[i][j - 1] + C, G[i][j])
            X[i][j] = min(dp[i][j - 1] + C + G[i][j], X[i][j])
        elif j == 0:
            dp[i][j] = min(dp[i - 1][j] + C, G[i][j])
            X[i][j] = min(dp[i - 1][j] + C + G[i][j], X[i][j])
        else:
            dp[i][j] = min(dp[i - 1][j] + C, dp[i][j - 1] + C, G[i][j])
            X[i][j] = min(dp[i][j - 1] + C + G[i][j], dp[i - 1][j] + C + G[i][j], X[i][j])
            ans = min(ans, X[i][j])
print(ans)
