"""
https://atcoder.jp/contests/arc138/submissions/30809339
"""

import sys
from sys import stdin
from collections import deque

N = int(stdin.readline())

A = deque(map(int, stdin.readline().split()))

for i in range(N + 1):
    b = i % 2

    if A[0] != b:
        break

    A.popleft()

    while A and A[-1] == b:
        A.pop()

    if len(A) == 0:
        break

if A:
    print("No")
else:
    print("Yes")
