import sys

sys.setrecursionlimit(2 * 10**6)
N = int(input())
G = [[] for _ in range(N)]
subtree = [0] * N
depth = [0] * N
ans = [0] * N


def dfs(G, v, p, d, mode="w"):
    if mode == "w":
        depth[v] = d
        for next_v in G[v]:
            if next_v == p:
                continue
            dfs(G, next_v, v, d + 1)
        subtree[v] = 1
        for c in G[v]:
            subtree[v] += subtree[c]
    else:
        for next_v in G[v]:
            if next_v == p:
                continue
            ans[next_v] = ans[v] + N - 2 * subtree[next_v]
            dfs(G, next_v, v, 0, mode="r")


for _ in range(N - 1):
    u, v = map(lambda x: int(x) - 1, input().split())
    G[u].append(v)
    G[v].append(u)
root = 0
# 探索(-1はv[0]の親がいないことを表す）
dfs(G, root, -1, 0)
ans[root] = sum(depth)
dfs(G, root, -1, 0, mode="r")
print(*ans, sep="\n")
f()
