from math import ceil

N = int(input())
inf = float("inf")
r = inf
l = -inf
ans = []
for i in range(N):
    L, R = map(int, input().split())
    r = min(r, R)
    l = max(l, L)
    if l <= r:
        ans.append(0)
    else:
        ans.append(ceil((l - r) / 2))
print(*ans, sep="\n")
