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

    L = input()
    N = len(L)

    dp = [[0, 0] for _ in range(N + 20)]
    dp[0][0] = 1
    MOD = 10**9 + 7
    for dgt in range(N):
        for isLess in range(2):
            if L[dgt] == "1":
                dp[dgt + 1][1] += dp[dgt][isLess]
                dp[dgt + 1][1] %= MOD
            else:
                dp[dgt + 1][isLess] += dp[dgt][isLess]
                dp[dgt + 1][isLess] %= MOD

            if L[dgt] == "1" or isLess:
                dp[dgt + 1][isLess] += dp[dgt][isLess] * 2
                dp[dgt + 1][isLess] %= MOD

    ans = sum(dp[N]) % MOD
    print(ans)


if __name__ == "__main__":
    main()
