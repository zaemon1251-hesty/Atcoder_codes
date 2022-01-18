H, W = map(int, input().split())
G = [list(input()) for _ in range(H)]
ans = 0
for i in range(H):
    for j in range(W):
        if G[i][j] == "#":
            continue
        dists = bfs(G, (i, j))
        dmax = max(max(dist) for dist in dists)
        ans = max(ans, dmax)
print(ans)
