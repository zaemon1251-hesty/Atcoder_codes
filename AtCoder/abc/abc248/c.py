def main():
    MOD = 998244353
    N, M, K = map(int, input().split())
    dp = [[0] * (K + 1) for i in range(N + 1)]
    dp[0][0] = 1
    for i in range(N):
        for ai in range(1, M + 1):
            for nxt in range(1, K + 1):
                if 0 <= nxt - ai <= K:
                    dp[i + 1][nxt] += dp[i][nxt - ai]
                    dp[i + 1][nxt] %= MOD
    print(sum(dp[N]) % MOD)


if __name__ == '__main__':
    main()
