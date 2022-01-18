import sys
import bisect
sys.setrecursionlimit(10**6)
N = int(input())
P = list(map(int, input().split()))
Q = int(input())
C = [[] for _ in range(N)]
for c, p in enumerate(P, 2):
    c -= 1
    p -= 1
    C[p].append(c)
tin = [-1] * N
tout = [-1] * N
dist = [-1] * N
dist[0] = 0
depth = [[] for _ in range(N)]
def dfs(now):
    global t
    tin[now] = t
    t += 1
    depth[dist[now]].append(tin[now])
    for to in C[now]:
        dist[to] = dist[now] + 1
        dfs(to)
    tout[now] = t
    t += 1
dfs(0)
for i in range(Q):
    u, d = map(int, input().split())
    u -= 1
    r = bisect.bisect_left(depth[d], tout[u])
    l = bisect.bisect_left(depth[d], tin[u])
    print(r - l)
_name__ == '__main__':
#maina()
#mainb()
#mainc()
#maind()
#maine()
mori = True