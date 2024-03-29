import sys

sys.setrecursionlimit(10**6)


def find(graph, start):
    res = [0]
    seen = [False] * n

    def dfs(v):
        seen[v] = True
        res[0] += 1
        for next_v in graph[v]:
            if seen[next_v]:
                continue
            dfs(next_v)

    dfs(start)

    return res[0]


n, m = map(int, input().split())
G = [[] for i in range(n)]
for i in range(m):
    n1, k1 = map(int, input().split())
    G[n1 - 1].append(k1 - 1)
ans = 0
for i in range(n):
    ans += find(G, i)
print(ans)
