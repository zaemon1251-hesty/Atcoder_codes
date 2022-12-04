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

    N, P = mi()
    MOD = 998244353
    INV = pow(100, MOD - 2, MOD)
    dp = [0] * (N + 1)
    dp[0] = 0
    dp[1] = 1

    for i in range(2, N + 1):
        dp[i] = dp[i - 2] * P * INV + dp[i - 1] * (100 - P) * INV + 1
        dp[i] %= MOD

    print(dp[N])


if __name__ == '__main__':
    main()
