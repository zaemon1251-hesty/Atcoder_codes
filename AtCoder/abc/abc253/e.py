def main():
    N, M, K = map(int, input().split())
    MOD = 998244353
    dp = [1] * (M + 1)
    dp[0] = 0
    if K == 0:
        print(pow(M, N, MOD))
        exit()
    for i in range(N - 1):
        inf_ = 0
        sup_ = sum(dp[K + 1:]) % MOD

        tmp = [1] * (M + 1)
        tmp[0] = 0

        for t in range(1, M + 1):
            if t - K >= 1:
                inf_ += dp[t - K]
                inf_ %= MOD
            tmp[t] = sup_ + inf_
            tmp[t] %= MOD
            if t + K <= M:
                sup_ -= dp[t + K]
                sup_ %= MOD

        dp = tmp
    res = 0
    for s in dp[1:]:
        res += s
        res %= MOD
    print(res % MOD)


if __name__ == '__main__':
    main()
