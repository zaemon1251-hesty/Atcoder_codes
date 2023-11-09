import sys


def input():
    return sys.stdin.readline().rstrip()


MOD = 10**9 + 7


def main():
    def li():
        return list(map(int, input().split()))

    def mi():
        return map(int, input().split())

    def ii():
        return int(input())

    N, M = mi()
    A = set([ii() for _ in range(M)])
    dp = [0] * (N + 1)
    dp[0] = 1
    for i in range(N + 1):
        if i in A:
            continue

        res = dp[i]

        if 0 <= i - 1:
            res += dp[i - 1]
            res %= MOD

        if 0 <= i - 2:
            res += dp[i - 2]
            res %= MOD

        dp[i] = res

    print(dp[N] % MOD)


if __name__ == "__main__":
    main()
