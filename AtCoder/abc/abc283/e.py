from collections import deque, defaultdict, Counter
from math import ceil
from bisect import *
from heapq import *
from itertools import product
import sys
import getpass

OFFLINE = getpass.getuser() == "zz"


def log(*args):
    if OFFLINE:
        print("\033[36m", *args, "\033[0m", file=sys.stderr)
    else:
        pass


def input():
    return sys.stdin.readline().strip()


def ri():
    return int(input())


def rri():
    return map(int, input().split())


inf = float("inf")
MOD = 998244353
R, C = rri()
A = []
for _ in range(R):
    A.append(list(rri()))

dp = [[[inf] * 2 for _ in range(2)] for _ in range(R + 1)]
dp[0][0][0] = 0
dp[0][0][1] = 1
for r in range(R):
    for x, y, z in product(range(2), repeat=3):
        for c in range(C):
            if not (
                r
                and A[r][c] ^ y == A[r - 1][c] ^ x
                or r < R - 1
                and A[r][c] ^ y == A[r + 1][c] ^ z
                or c
                and A[r][c] ^ y == A[r][c - 1] ^ y
                or c < C - 1
                and A[r][c] ^ y == A[r][c + 1] ^ y
            ):
                break
        else:
            dp[r + 1][y][z] = min(dp[r + 1][y][z], dp[r][x][y] + z)

ans = inf
for x in range(2):
    for y in range(2):
        ans = min(ans, dp[R][x][y])

print(ans if ans < inf else -1)
