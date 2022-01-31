#!/usr/local/bin/pypy3

# LIS 最長増加部分列
from bisect import bisect_left
import sys
readline = sys.stdin.buffer.readline
sys.setrecursionlimit(10**6)

n = int(readline())
p = list(map(int, readline().split()))
q = list(map(int, readline().split()))

pos = [0]*(n+1)
for i in range(n):
    pos[q[i]] = i

z = [10**9]*n
for i in p:
    ls = []
    for j in range(i, n+1, i):
        ls.append(pos[j])
    ls.sort()
    ls.reverse()
    for j in ls:
        z[bisect_left(z, j)] = j

print(bisect_left(z, 10**9))
