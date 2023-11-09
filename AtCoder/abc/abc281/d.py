import sys
from math import inf


def input():
    return sys.stdin.readline().rstrip()


def main():
    def li():
        return list(map(int, input().split()))

    def mi():
        return map(int, input().split())

    def ii():
        return int(input())

    N, K, D = mi()
    A = li()

    dp = [[[-inf] * D for _ in range(N + 1)] for _ in range(K + 1)]
    dp[0][0][0] = 0

    for k in range(K):
        for i in range(N):
            a = A[i]
            for d in range(D):
                dp[k][i + 1][d] = max(dp[k][i + 1][d], dp[k][i][d])
            for d in range(D):
                dp[k + 1][i + 1][(d + a) % D] = max(
                    dp[k + 1][i + 1][(d + a) % D],
                    dp[k][i][d] + a,
                )

    ans = max([dp[K][i][0] for i in range(N + 1)])

    print(ans if ans > -inf else -1)


if __name__ == "__main__":
    main()
