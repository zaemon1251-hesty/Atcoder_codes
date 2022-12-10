import sys
sys.setrecursionlimit(1000000)

n, m = map(int, input().split())

# この問題特有の設定
counter = [0] * n


def dfs(G, v, p, x):
    counter[v] += x
    for next_v in G[v]:
        if next_v == p:
            continue
        dfs(G, next_v, v, counter[v])


G = [[] for _ in range(n)]
for i in range(n - 1):
    a, b = map(lambda x: int(x) - 1, input().split())
    G[a].append(b)
    G[b].append(a)

for j in range(m):
    p, x = map(int, input().split())
    p -= 1
    counter[p] += x

# v[0]を根とする
root = 0
# 探索(-1はv[0]の親がいないことを表す）
dfs(G, root, -1, 0)

print(*counter, sep=' ')
