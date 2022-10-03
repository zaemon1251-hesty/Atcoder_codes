from math import inf
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

    N, M, K = mi()
    edges = [li() for _ in range(M)]
    E = li()
    dp = [inf] * N
    dp[0] = 0

    for k in range(K):
        i = E[k] - 1
        ai, bi, ci = edges[i]
        ai -= 1
        bi -= 1
        dp[bi] = min(dp[bi], dp[ai] + ci)

    print(-1 if dp[-1] == inf else dp[-1])


if __name__ == '__main__':
    main()
