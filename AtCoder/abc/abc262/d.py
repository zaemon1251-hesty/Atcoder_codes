MOD = 998244353


def main():
    N = int(input())
    A = list(map(int, input().split()))
    ans = 0
    for modp in range(1, N + 1):

        dp = [[[0] * (modp + 10) for _ in range(modp + 1)]
              for _ in range(N + 1)]
        dp[0][0][0] = 1

        for i in range(N):
            for j in range(modp + 1):
                for k in range(modp):
                    dp[i + 1][j][k] += dp[i][j][k]
                    dp[i + 1][j][k] %= MOD
                    if j < modp:
                        dp[i + 1][j + 1][(k + A[i]) % modp] += dp[i][j][k]
                        dp[i + 1][j + 1][(k + A[i]) % modp] %= MOD

        ans += dp[N][modp][0]
        ans %= MOD
    print(ans)


if __name__ == '__main__':
    main()
