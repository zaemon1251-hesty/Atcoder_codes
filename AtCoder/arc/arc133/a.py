#!/usr/local/bin/pypy3
import sys

readline = sys.stdin.buffer.readline
sys.setrecursionlimit(10**6)

n = int(readline())
a = list(map(int, readline().split()))

x = a[-1]
for i in range(n - 1):
    if a[i] > a[i + 1]:
        x = a[i]
        break

a = [v for v in a if v != x]
print(*a)
