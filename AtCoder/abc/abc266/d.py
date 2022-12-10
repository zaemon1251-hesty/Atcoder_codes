from collections import defaultdict
from math import inf
import sys
input = sys.stdin.readline


def main():
    N = int(input())
    TXA = [list(map(int, input().split())) for _ in range(N)]
    w = [defaultdict(int) for _ in range(5)]
    dp = [[-inf] * 5 for _ in range(10**5 + 1)]
    dp[0][0] = 0

    for t, x, a in TXA:
        w[x][t] = a

    for i in range(1, 10**5 + 1):
        for loc in range(5):
            newv = dp[i - 1][loc]
            if loc < 4:
                newv = max(newv, dp[i - 1][loc + 1])
            if loc > 0:
                newv = max(newv, dp[i - 1][loc - 1])
            dp[i][loc] = max(dp[i][loc], newv + w[loc][i])
    print(max(dp[-1]))


if __name__ == '__main__':
    main()
