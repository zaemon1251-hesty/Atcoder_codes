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

    N = ii()
    X = map(int, list(input()))
    X = list(X)
    dp = [0] * (N + 1)
    S = [0] * (N + 1)

    dp[0] = 1
    S[0] = S[-1] + dp[0]

    dp[1] = X[0]
    S[1] = S[0] + dp[1]

    for i in range(1, N):
        dp[i + 1] = (10 * dp[i] + X[i] * S[i]) % 998244353
        S[i + 1] = (S[i] + dp[i + 1]) % 998244353
    print(dp[N])
