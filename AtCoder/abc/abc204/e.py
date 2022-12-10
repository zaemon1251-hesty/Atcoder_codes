from heapq import heappop, heappush
from sys import stdin


def input():
    return stdin.readline().rstrip()


n, m = map(int, input().split())
g = [[] for i in range(n)]
for i in range(m):
    a, b, c, d = map(int, input().split())
    a, b = a - 1, b - 1
    g[a].append((b, c, d))
    g[b].append((a, c, d))

infty = 10 ** 20


def get_dist(now, c, d):
    to = int(d ** .5) - 1
    return min(t - now + c + d // (t + 1)
               for t in [to, to + 1, now] if t >= now)


q = []
dist = [infty] * n
q.append((0, 0))
dist[0] = 0
while q:
    t, v = heappop(q)
    if dist[v] != t:
        continue
    for nv, c, d in g[v]:
        nd = get_dist(t, c, d)
        if dist[nv] > t + nd:
            dist[nv] = t + nd
            heappush(q, (t + nd, nv))
ans = dist[n - 1]
if ans == infty:
    ans = -1
print(ans)
