from collections import defaultdict as dd
from heapq import *

M = 10**9
T = int(input())
for _ in range(T):
    N = int(input())
    R = dd(list)
    R[2 * M].append(2 * M)
    for _ in range(N):
        l, r = map(int, input().split())
        R[l].append(r)
    now = 1
    hq = []
    K = sorted(R.keys())
    flag = 1
    for i in range(len(K) - 1):
        k = K[i]
        now = max(now, k)
        for r in R[k]:
            heappush(hq, r)
        while hq and now < K[i + 1]:
            r = heappop(hq)
            if now > r:
                flag = 0
            now += 1
    print('Yes' if flag else 'No')
