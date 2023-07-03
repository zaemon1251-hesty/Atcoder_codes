import sys

MOD = 998244353


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
    dp = [[0] * 2 for _ in range(N + 1)]
    dp[0][1] = 1
    for i in range(N):
        dp[i + 1][0] = (dp[i][0] * (M - 2) + dp[i][1] * (M - 1)) % MOD
        dp[i + 1][1] = dp[i][0] % MOD
    print((dp[N][1] * M) % MOD)


if __name__ == "__main__":
    main()
