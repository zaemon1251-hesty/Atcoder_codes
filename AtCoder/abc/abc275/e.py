import sys
sys.setrecursionlimit(10**6)


def input():
    return sys.stdin.readline().rstrip()


MOD = 998244353


def main():
    def li():
        return list(map(int, input().split()))

    def mi():
        return map(int, input().split())

    def ii():
        return int(input())

    N, M, K = mi()
    MINV = pow(M, MOD - 2, MOD)

    dp = [[0] * (N + 1) for _ in range(K + 1)]
    dp[0][0] = 1

    for k in range(K):
        for cur in range(N):
            for t in range(1, M + 1):
                nxt = cur + t
                if nxt > N:
                    nxt = 2 * N - nxt
                dp[k + 1][nxt] = (dp[k + 1][nxt] + dp[k][cur] * MINV) % MOD
        dp[k + 1][N] = (dp[k + 1][N] + dp[k][N]) % MOD
    print(dp[K][N])


if __name__ == '__main__':
    main()
