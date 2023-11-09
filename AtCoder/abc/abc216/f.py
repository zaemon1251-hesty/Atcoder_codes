def main():
    MOD = 998244353
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    AB = sorted(zip(A, B), key=lambda x: x[0])

    dp = [[0] * (5050) for _ in range(N + 1)]
    colTotal = [0] * (5050)

    dp[0][0] = 1
    colTotal[0] = 1

    for i in range(N):
        for tot in range(5050):
            if 0 <= tot - AB[i][1]:
                dp[i + 1][tot] += colTotal[tot - AB[i][1]]
                dp[i + 1][tot] %= MOD
        for tot in range(5050):
            colTotal[tot] += dp[i + 1][tot]
            colTotal[tot] %= MOD

    ans = 0
    for i in range(N):
        ans += sum(dp[i + 1][: AB[i][0] + 1])
        ans %= MOD
    print(ans)


if __name__ == "__main__":
    main()
