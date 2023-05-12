# ABC180-E Traveling Salesman among Aerial Cities
N = int(input())
inf = 10**18
x = []
y = []
z = []
for i in range(N):
    a, b, c = map(int, input().split())
    x.append(a)
    y.append(b)
    z.append(c)

cost = [[inf] * N for _ in range(N)]
keiro = [[[] for _ in range(N)] for _ in range(N)]
# warshall_floyd
for k in range(N):
    for i in range(N):
        for j in range(N):
            if cost[i][j] == inf:
                cost[i][j] = abs(x[j] - x[i]) + abs(y[j] - y[i]) + max(0, z[j] - z[i])
            else:
                if cost[i][j] > cost[i][k] + cost[k][j]:
                    cost[i][j] = cost[i][k] + cost[k][j]
                    keiro[i][j].append(k)

# bitDP
# dp[s][i]は頂点集合sを全て通って頂点iで終わる道のうち最小となる辺の数
dp = [[inf] * (N) for _ in range(2**N)]

# bitDPの部分,k!の問題を(2^k)(k^2)で解ける
for s in range(1, 2**N):
    for i in range(N):
        if s == (1 << i):
            p = s
            for t in keiro[0][i]:
                p |= 1 << t
            dp[p][i] = cost[0][i]
        elif (s >> i) & 1:
            for j in range(N):
                p = s
                for t in keiro[0][i]:
                    p |= 1 << t
                dp[p][i] = min(dp[p][i], dp[p ^ (1 << i)][j] + cost[j][i])


ans = inf
for i in range(N):
    ans = min(ans, dp[-1][i] + cost[i][0])
print(ans)
