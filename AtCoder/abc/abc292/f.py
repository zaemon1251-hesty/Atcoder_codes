from sys import stdin
from math import sqrt

# 空白区切りの整数を一行読み込み
# list<int>


def LI(): return list(map(int, stdin.readline().rstrip().split()))


A, B = LI()

M = max(A, B)
m = min(A, B)

tan = min((2 * M / m) - sqrt(3), 1 / sqrt(3))

print(m * sqrt(1 + tan**2))
