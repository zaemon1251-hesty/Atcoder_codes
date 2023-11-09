from itertools import combinations
from math import inf, sqrt
import sys


def input():
    return sys.stdin.readline().rstrip()


popcount = [0] * 32
for i in range(1, 32):
    popcount[i] = popcount[i // 2] + (i % 2)


def main():
    def li():
        return list(map(int, input().split()))

    def mi():
        return map(int, input().split())

    def ii():
        return int(input())

    N, M = mi()
    TOWN = [li() for _ in range(N)]
    BOX = [li() for _ in range(M)]
    D = {}

    def distance(i, j):
        if i is not None:
            x = BOX[i - N] if i >= N else TOWN[i]
        else:
            x = [0, 0]
        if j is not None:
            y = BOX[j - N] if j >= N else TOWN[j]
        else:
            y = [0, 0]
        return sqrt(sum((yi - xi) ** 2 for xi, yi in zip(x, y)))

    for i, j in combinations(range(N + M), 2):
        D[i, j] = D[j, i] = distance(i, j)

    for i in range(N + M):
        D[None, i] = D[i, None] = distance(None, i)

    dp = [[inf] * (1 << (N + M)) for _ in range(N + M)]

    # 原点から
    for i in range(N + M):
        dp[i][1 << i] = D[None, i]

    # 町と宝箱
    for s in range(1, 1 << (N + M)):
        coef = 0.5 ** popcount[s >> N]
        for i in range(N + M):
            if not (s >> i) & 1:
                continue
            for j in range(N + M):
                if (s >> j) & 1:
                    continue
                dp[j][s ^ (1 << j)] = min(dp[j][s ^ (1 << j)], dp[i][s] + D[i, j] * coef)

    # 原点へ
    alltowns = sum(1 << y for y in range(N))
    ans = inf
    for s in range(1 << (N + M)):
        coef = 0.5 ** popcount[s >> N]
        if s & alltowns != alltowns:
            continue
        for i in range(N + M):
            ans = min(ans, dp[i][s] + D[i, None] * coef)

    print(ans)


if __name__ == "__main__":
    main()
