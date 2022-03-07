def main():
    MOD = 998244353
    N = int(input())
    dp = [1] * 9
    for _ in range(N - 1):
        tmp = [0] * 9
        for d in range(9):
            tmp[d] += dp[d]
            if d > 0:
                tmp[d] += dp[d - 1]
            if d < 8:
                tmp[d] += dp[d + 1]
            dp[d] %= MOD
        dp = tmp
    print(sum(dp) % MOD)


if __name__ == '__main__':
    main()
