from collections import deque

n, u, v = map(int, input().split())
u -= 1
v -= 1
graph = [[] for _ in range(n)]


for _ in range(n - 1):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    graph[a].append(b)
    graph[b].append(a)

isleaf = [False] * n


def bfs(s):
    dq = deque()
    dq.append(s)
    dist = [-1] * n
    dist[s] = 0

    while dq:
        u = dq.popleft()
        for v in graph[u]:
            if dist[v] == -1:
                dist[v] = dist[u] + 1
                dq.append(v)

    return dist


u_dist = bfs(u)
v_dist = bfs(v)

for i in range(n):
    if len(graph[i]) == 1:
        isleaf[i] = True

ans = 0
max_dist = -1

for i, (d1, d2) in enumerate(zip(u_dist, v_dist)):
    if isleaf[i] and max_dist < d2 and d1 < d2:
        max_dist = d2

print(max_dist - 1)
