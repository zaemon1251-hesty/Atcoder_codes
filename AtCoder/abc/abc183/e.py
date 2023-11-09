def main():
    H, W = map(int, input().split())
    S = [list(input()) for _ in range(H)]
    dp = [[0] * W for _ in range(H)]
    X = [0] * H
    Y = [0] * W
    t = max(H, W)
    Z = {i: 0 for i in range(-t, t + 1)}
    MOD = 10**9 + 7
    dp[0][0] = 1
    for i in range(H):
        for j in range(W):
            if S[i][j] == "#":
                X[i] = 0
                Y[j] = 0
                Z[j - i] = 0
                continue
            dp[i][j] += X[i] + Y[j] + Z[j - i]
            dp[i][j] %= MOD
            X[i] += dp[i][j]
            X[i] %= MOD
            Y[j] += dp[i][j]
            Y[j] %= MOD
            Z[j - i] += dp[i][j]
            Z[j - i] %= MOD
    print(dp[H - 1][W - 1])


if __name__ == "__main__":
    main()
