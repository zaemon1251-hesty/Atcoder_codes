from typing import List, Tuple, Optional
import sys
import itertools
import heapq
import bisect
import math
from collections import deque, defaultdict
from functools import lru_cache, cmp_to_key

input = sys.stdin.readline

if __file__ != 'prog.py':
    sys.setrecursionlimit(10 ** 6)


def readints(): return map(int, input().split())
def readlist(): return list(readints())
def readstr(): return input()[:-1]


class WeightedUnionFind:
    "ポテンシャル付きUnionFind"

    def __init__(self, N):
        self.N = N
        self.par = [-1] * N
        self.weight = [0] * N

    def find(self, x):
        if self.par[x] < 0:
            return x
        p = self.find(self.par[x])
        self.weight[x] += self.weight[self.par[x]]
        self.par[x] = p
        return self.par[x]

    def merge(self, x, y, z):
        "Wy = Wx + z"
        x_, y_ = x, y
        x = self.find(x)
        y = self.find(y)
        wx = self.weight[x_]
        wy = self.weight[y_]

        if x == y:
            return False
        if self.par[x] > self.par[y]:
            x, y = y, x
            wx, wy = wy, wx
            z = -z

        self.par[x] += self.par[y]
        self.par[y] = x
        self.weight[y] = z + wx - wy
        return True

    def diff(self, x, y):
        "return Wy - Wx if calculable otherwise None"
        if self.find(x) != self.find(y):
            return None
        return self.weight[y] - self.weight[x]


N, M, Q = readints()
uf = WeightedUnionFind(N)
flag = [False] * N
for _ in range(M):
    a, b, c = readints()
    a -= 1
    b -= 1
    diff = uf.diff(a, b)
    if diff is None:
        uf.merge(a, b, c)
        continue
    if diff != c:
        flag[uf.find(a)] = True
for _ in range(Q):
    x, y = readints()
    x -= 1
    y -= 1
    diff = uf.diff(x, y)
    if diff is None:
        print('nan')
    elif flag[uf.find(x)]:
        print('inf')
    else:
        print(diff)
