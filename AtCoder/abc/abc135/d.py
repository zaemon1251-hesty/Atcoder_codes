def main():
    S = list(input())
    N = len(S)
    MOD = 10**9 + 7
    dp = [[0] * 13 for _ in range(N + 1)]
    dp[0][0] = 1

    for i in range(N):
        if S[i] == "?":
            for k in range(10):
                for r in range(13):
                    res = dp[i + 1][(10 * r + k) % 13]
                    res += dp[i][r]
                    res %= MOD
                    dp[i + 1][(10 * r + k) % 13] = res
        else:
            k = int(S[i])
            for r in range(13):
                res = dp[i + 1][(10 * r + k) % 13]
                res += dp[i][r]
                res %= MOD
                dp[i + 1][(10 * r + k) % 13] = res
    print(dp[N][5])


if __name__ == '__main__':
    main()
