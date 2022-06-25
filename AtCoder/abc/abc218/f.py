from collections import deque

n, m = map(int, input().split())
adj = [set() for _ in range(n)]
edges = []
for _ in range(m):
    u, v = map(int, input().split())
    u -= 1
    v -= 1
    adj[u].add(v)
    edges.append((u, v))


def bfs(adj, n, src=0):
    dist = [-1] * n
    pred = [-1] * n
    dist[src] = 0
    q = deque()
    q.append(src)
    while q:
        u = q.popleft()
        for v in adj[u]:
            if dist[v] == -1:
                dist[v] = dist[u] + 1
                pred[v] = u
                q.append(v)
    return dist, pred


dist, pred = bfs(adj, n)
for i in range(m):
    u, v = edges[i]
    if pred[v] == u:
        adj[u].remove(v)
        print(bfs(adj, n)[0][n - 1])
        adj[u].add(v)
    else:
        print(dist[n - 1])
