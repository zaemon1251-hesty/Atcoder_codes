MOD = 998244353


def main():
    N, S = map(int, input().split())
    A = list(map(int, input().split()))
    dp = [[0] * 6000 for _ in range(N + 1)]
    dp[0][0] = pow(2, N, MOD)
    for i in range(N):
        for k in range(S + 1):
            dp[i + 1][k] += dp[i][k]
            dp[i + 1][k] %= MOD
            dp[i + 1][k + A[i]] += dp[i][k] * pow(2, MOD - 2, MOD)
            dp[i + 1][k + A[i]] %= MOD
    print(dp[N][S])


if __name__ == '__main__':
    main()
