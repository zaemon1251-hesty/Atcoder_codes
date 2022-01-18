import sys
from collections import defaultdict
sys.setrecursionlimit(10**6)
mod = 998244353
N, M, K = map(int, input().split())
A = list(map(int, input().split()))
E = [0]*(N-1)
G = [[] for _ in range(N)]
for i in range(N-1):
    u, v = map(int, input().split())
    u -= 1
    v -= 1
    G[u].append([v, i])
    G[v].append([u, i])
for i in range(M-1):
    s = A[i]-1
    g = A[i+1]-1
    def dfs(G, v, p):
        if v == g:
            return True
        for next_v, e in G[v]:
            if next_v == p:
                continue
            if dfs(G, next_v, v):
                E[e] += 1
                return True
        return False
    dfs(G, s, -1)
S = sum(E)
if (S + K) % 2 != 0 or S + K < 0 or S - K < 0:
    print(0)
    exit()
R = min((S + K) // 2, (S - K) // 2)
dp = [0 for _ in range(R + 1)]
dp[0] = 1
for v in E:
    if E == 0:
        continue
    for c in range(R, v-1, -1):
        dp[c] += dp[c-v]
        dp[c] %= mod
print(dp[R] % mod)
e()
