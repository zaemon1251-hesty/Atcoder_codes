R, C, K = map(int, input().split())
G = [[0]*C for _ in range(R)]
dp = [[[0]*4 for _ in range(C)]for _ in range(R)]
for _ in range(K):
    r, c, v = map(int, input().split())
    G[r-1][c-1] = v
    #dp[r-1][c-1][0] = v
for i in range(R):
    for k in range(3):
        for j in range(C):
            i_prev = max(dp[i-1][j])
            if i == j == 0:
                dp[i][j][k+1] = G[i][j] if k+1 == 1 else 0
            elif i == 0:
                dp[i][j][k+1] = max(
                    dp[i][j][k+1],
                    dp[i][j-1][k+1],
                    dp[i][j-1][k] + G[i][j]
                )
            elif j == 0:
                dp[i][j][k+1] = max(
                    dp[i][j][k+1],
                    i_prev + G[i][j]
                )
            else:
                dp[i][j][k+1] = max(
                    dp[i][j][k+1],
                    dp[i][j-1][k+1],
                    dp[i][j-1][k] + G[i][j],
                    i_prev + G[i][j]
                )
print(max(dp[-1][-1]))
