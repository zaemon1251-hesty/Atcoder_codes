import sys
import random
import bisect
from collections import deque, defaultdict
from heapq import heapify, heappop, heappush
from itertools import permutations
from math import gcd, log


def input():
    return sys.stdin.readline().rstrip()


def mi():
    return map(int, input().split())


def li():
    return list(mi())


def main():
    H, W = mi()
    R = li()
    C = li()
    A = [input() for i in range(H)]

    dp = [[10**17 for i in range(4)] for i in range(W)]
    dp[0][0] = 0
    dp[0][1] = R[0]
    dp[0][2] = C[0]
    dp[0][3] = R[0] + C[0]

    for i in range(H):
        for j in range(W - 1):
            if A[i][j] == A[i][j + 1]:
                dp[j + 1][0] = min(dp[j + 1][0], dp[j][0])
                dp[j + 1][1] = min(dp[j + 1][1], dp[j][1])
                dp[j + 1][2] = min(dp[j + 1][2], dp[j][2] + C[j + 1])
                dp[j + 1][3] = min(dp[j + 1][3], dp[j][3] + C[j + 1])
            else:
                dp[j + 1][0] = min(dp[j + 1][0], dp[j][2])
                dp[j + 1][1] = min(dp[j + 1][1], dp[j][3])
                dp[j + 1][2] = min(dp[j + 1][2], dp[j][0] + C[j + 1])
                dp[j + 1][3] = min(dp[j + 1][3], dp[j][1] + C[j + 1])

        if i == H - 1:
            break

        c = R[i + 1]

        for j in range(W):
            if A[i][j] == A[i + 1][j]:
                dp[j] = [dp[j][0], dp[j][1] + c, dp[j][2], dp[j][3] + c]
            else:
                dp[j] = [dp[j][1], dp[j][0] + c, dp[j][3], dp[j][2] + c]

    print(min(dp[W - 1]))


if __name__ == "__main__":
    main()
