"""
TODO
https://atcoder.jp/contests/abc247/submissions/30896431
"""
MOD = 998244353
N = int(input())
P = list(map(lambda x: int(x) - 1, input().split()))
Q = list(map(lambda x: int(x) - 1, input().split()))


R = [0] * N
for i in range(N):
    R[P[i]] = Q[i]

DP1 = [[0, 0] for _ in range(N + 1)]
DP2 = [[0, 0] for _ in range(N + 1)]
DP1[1][0] = 1
DP2[1][1] = 1
for i in range(2, N + 1):
    DP1[i][0] = DP1[i - 1][1]
    DP1[i][1] = DP1[i - 1][0] + DP1[i - 1][1] % MOD
    DP2[i][0] = DP2[i - 1][1]
    DP2[i][1] = DP2[i - 1][0] + DP2[i - 1][1] % MOD

ans = 1
visited = [False] * N
for i in range(N):
    if visited[i]:
        continue
    size = 0
    while not visited[i]:
        size += 1
        visited[i] = True
        i = R[i]
    ans *= DP1[size][1] + DP2[size][0] + DP2[size][1] % MOD
    ans %= MOD
print(ans)
