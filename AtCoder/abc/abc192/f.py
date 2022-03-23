def main():
    inf = 1 << 60
    N, X = map(int, input().split())
    A = list(map(int, input().split()))

    ans = inf
    for k in range(1, N + 1):
        # dp[i][use][r]] = i番目まででuseコ使って初期合計魔力が r[mod k] のときの残り魔力の最小値
        dp = [[
            [inf] * 101
            for _ in range(101)]
            for _ in range(101)]
        dp[0][0][X % k] = X
        for i in range(N):
            for use in range(k + 1):
                for r in range(k):
                    if dp[i + 1][use][r] > dp[i][use][r]:
                        dp[i + 1][use][r] = dp[i][use][r]
                    next_resd = (((r - A[i]) % k) + k) % k
                    if use < k and \
                            dp[i + 1][use + 1][next_resd] > dp[i][use][r] - A[i]:
                        dp[i + 1][use + 1][next_resd] = dp[i][use][r] - A[i]
        if dp[N][k][0] != inf:
            ans = min(ans, dp[N][k][0] // k)
    print(ans)


if __name__ == '__main__':
    main()
