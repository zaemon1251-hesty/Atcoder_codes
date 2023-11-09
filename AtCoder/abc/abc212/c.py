mod = 998244353
N, M, K = map(int, input().split())
G = [[] for _ in range(N)]
P = []
dp = [0] * N
dp[0] = 1
for _ in range(M):
    u, v = map(int, input().split())
    u -= 1
    v -= 1
    G[u].append(v)
    G[v].append(u)
    P.append((u, v))
for i in range(K):
    tmp = [sum(dp) % mod] * N
    for i in range(N):
        tmp[i] -= dp[i]
    for u, v in P:
        tmp[u] -= dp[v]
        tmp[u] %= mod
        tmp[v] -= dp[u]
        tmp[u] %= mod
    dp = tmp
print(dp[0] % mod)
e()
