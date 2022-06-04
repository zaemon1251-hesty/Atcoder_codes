from collections import deque
import sys
sys.setrecursionlimit(10**6)


N, M = map(int, input().split())
G = [[] for _ in range(N)]
for _ in range(M):
    a, b = map(int, input().split())
    G[a - 1].append(b - 1)
    G[b - 1].append(a - 1)


def dfs(u):
    global T1
    visited[u] = True
    for v in G[u]:
        if not visited[v]:
            T1.append((u + 1, v + 1))
            dfs(v)


def bfs(s):
    dist = [-1] * N
    dist[s] = 0
    edges = []
    que = deque([s])
    while que:
        u = que.popleft()
        for v in G[u]:
            if dist[v] == -1:
                dist[v] = dist[u] + 1
                edges.append((u + 1, v + 1))
                que.append(v)
    return edges


T1 = []
visited = [False] * N
dfs(0)
T2 = bfs(0)

for u, v in T1:
    print(u, v)
for u, v in T2:
    print(u, v)
