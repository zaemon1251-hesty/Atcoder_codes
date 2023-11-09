import heapq

Z = 2500
N, M, S = map(int, input().split())
S = min(S, Z)
links = [[] for _ in range(N)]
for _ in range(M):
    u, v, a, b = map(int, input().split())
    u -= 1
    v -= 1
    links[u].append((v, a, b))
    links[v].append((u, a, b))

P = [tuple(map(int, input().split())) for _ in range(N)]

inf = float("inf")
visited = [[inf] * (Z + 1) for _ in range(N)]
visited[0][S] = 0
hq = [(0, 0, S)]
while hq:
    p, x, s = heapq.heappop(hq)
    if p > visited[x][s]:
        continue

    for nx, a, b in links[x]:
        if s >= a:
            ns = s - a
            np = p + b
            if np < visited[nx][ns]:
                visited[nx][ns] = np
                heapq.heappush(hq, (np, nx, ns))

    c, d = P[x]
    ns = min(Z, s + c)
    np = p + d
    nx = x
    if np < visited[nx][ns]:
        visited[nx][ns] = np
        heapq.heappush(hq, (np, nx, ns))

for i in range(1, N):
    print(min(visited[i]))
