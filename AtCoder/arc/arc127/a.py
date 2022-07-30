import heapq
import sys
from collections import defaultdict, deque
from math import inf
sys.setrecursionlimit(10**6)
MOD = 10**9 + 7

stdin = sys.stdin

ni = lambda: int(ns())
na = lambda: list(map(int, stdin.readline().split()))
ns = lambda: stdin.readline().rstrip()  # ignore trailing spaces
x = ni()
n = str(x)
l = len(n)
ans = 0
for num_ones in range(1, l+1):
    for num_zeros in range(0, l+1):
        if num_ones + num_zeros > l: break
        a = int('1' * num_ones + '0' * num_zeros)
        if a > x: break
        b = int('1' * (num_ones-1) + '2' + '0' * num_zeros)
        ans += min(x+1,b) - a
print(ans)

