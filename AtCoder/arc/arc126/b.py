import sys
from bisect import bisect_left

N, M = map(int, sys.stdin.readline().split())
m = map(int, sys.stdin.read().split())
AB = sorted(zip(m, m), key=lambda x: (x[0], -x[1]))

INF = 1 << 30
LIS = [INF] * (N + 1)
for a, b in AB:
    i = bisect_left(LIS, b)
    LIS[i] = b

ANS = bisect_left(LIS, INF)
print(ANS)
