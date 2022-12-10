N = int(input())
xyz = []
for _ in range(N):
    xyz.append(list(map(int, input().split())))
dist = [[0]*N for _ in range(N)]
for i in range(N):
    for j in range(N):
        xi, yi, zi = xyz[i]
        xj, yj, zj = xyz[j]
        dist[i][j] = abs(xi-xj) + abs(yi-yj) + max(0, zj-zi)

dp = [[float('inf')]*N for _ in range(2**N)]
dp[0][0] = 0
msk = 2**N - 1
for s in range(2**N):
    for v in range(N):
        for u in range(N):
            if s == 0:
                s1 = 1 << v
                dp[s1][v] = min(dp[s1][v], dp[0][u]+dist[u][v])
            else:
                if (s >> v) & 1:
                    continue
                if not (s >> u) & 1:
                    continue
                s1 = s | (1 << v)
                dp[s1][v] = min(dp[s1][v], dp[s][u]+dist[u][v])

print(dp[2**N-1][0])
