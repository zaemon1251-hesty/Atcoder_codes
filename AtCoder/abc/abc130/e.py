import sys


def input():
    return sys.stdin.readline().rstrip()


def main():
    def li():
        return list(map(int, input().split()))

    def mi():
        return map(int, input().split())

    def ii():
        return int(input())

    N, M = mi()
    S = li()
    T = li()
    MOD = 10**9 + 7
    dp = [[0] * (M + 10) for _ in range(N + 10)]
    dp[0][0] = 1
    for i in range(N + 1):
        for j in range(M + 1):
            res = dp[i][j] % MOD
            if i > 0 and j > 0 and S[i - 1] == T[j - 1]:
                res += dp[i - 1][j - 1] % MOD
            if i > 0:
                res += dp[i - 1][j] % MOD
            if j > 0:
                res += dp[i][j - 1] % MOD
            if i > 0 and j > 0:
                res -= dp[i - 1][j - 1] % MOD

            dp[i][j] = res % MOD
    print(dp[N][M])


if __name__ == '__main__':
    main()
