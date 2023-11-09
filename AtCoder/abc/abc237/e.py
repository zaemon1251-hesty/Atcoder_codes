from collections import deque


N, M = map(int, input().split())
(*H,) = map(int, input().split())
T = [tuple(map(int, input().split())) for _ in range(M)]
G = [[] for _ in range(N)]
inf = 1 << 60
for u, v in T:
    u -= 1
    v -= 1
    G[v].append(u)
    G[u].append(v)

todo = deque([0])
dist = [inf] * N
dist[0] = 0
while todo:
    i = todo.popleft()
    for p in G[i]:
        d = H[p] - H[i]
        tw = 2 if d > 0 else 1
        nv = tw * d + dist[i]
        if nv < dist[p]:
            dist[p] = min(nv, dist[p])
            todo.append(p)
print(-min(dist))
