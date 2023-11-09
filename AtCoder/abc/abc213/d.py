sys.setrecursionlimit(10**6)
n = int(input())
G = [[] for _ in range(n)]
for i in range(n - 1):
    a, b = map(lambda x: int(x) - 1, input().split())
    G[a].append(b)
    G[b].append(a)
seen = [False] * n
ans = []
fl = False


def dfs(G, v):
    if v == 0 and fl:
        return
    seen[v] = True
    ans.append(v + 1)
    for next_v in sorted(G[v]):
        if seen[next_v] == True:
            continue
        dfs(G, next_v)
        if ans[-1] != v + 1:
            ans.append(v + 1)
        fl = True
    if ans[-1] != v + 1:
        ans.append(v + 1)


dfs(G, 0)
print(*ans, sep=" ")
