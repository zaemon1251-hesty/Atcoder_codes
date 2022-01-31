n, m = map(int, input().split())
mod = 998244353

DP = [[[[0 for _ in range(m + 1)] for _ in range(m + 1)]
       for _ in range(m + 1)] for _ in range(n + 1)]
DP[0][m][m][m] = 1
for i in range(n):
    for j in range(m + 1):
        for k in range(m + 1):
            for l in range(m + 1):
                for x in range(m):
                    if x <= j:
                        DP[i + 1][x][k][l] += DP[i][j][k][l]
                        DP[i + 1][x][k][l] %= mod
                    elif x <= k:
                        DP[i + 1][j][x][l] += DP[i][j][k][l]
                        DP[i + 1][j][x][l] %= mod
                    elif x <= l:
                        DP[i + 1][j][k][x] += DP[i][j][k][l]
                        DP[i + 1][j][k][x] %= mod

ans = 0
for i in range(m):
    for j in range(i + 1, m):
        for k in range(j + 1, m):
            ans += DP[n][i][j][k]
            ans %= mod
print(ans)
