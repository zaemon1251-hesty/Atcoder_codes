def main():
    N, M = map(int, input().split())
    MOD = 998244353
    if 60 < N:
        print(0)
        exit()

    dp = [0] * 61
    k = 1
    store = M
    while store:
        sub = min(pow(2, k - 1), store)
        dp[k] = sub
        store -= sub
        k += 1

    for i in range(N - 1):
        tmp = [0] * 61
        total = 0
        store = M
        k = 1
        while store:
            sub = min(pow(2, k - 1), store)

            tmp[k] = sub * total
            tmp[k] %= MOD

            total += dp[k]
            total %= MOD

            store -= sub
            k += 1
        dp = tmp

    print(sum(dp) % MOD)


if __name__ == '__main__':
    main()
