from collections import deque

mod = 10**9 + 7
inf = 1 << 60
N, M = map(int, input().split())
G = [[] for _ in range(N)]
for _ in range(M):
    a, b = list(map(lambda x: int(x) - 1, input().split()))
    G[a].append(b)
    G[b].append(a)
cnt = [0] * N
cnt[0] = 1
dist = [inf] * N
todo = deque([0])
dist[0] = 0
while todo:
    v = todo.popleft()
    for next_v in G[v]:
        # bfsだから深さd以下の頂点はもう更新されない
        if dist[next_v] == inf:
            dist[next_v] = dist[v] + 1
            cnt[next_v] = cnt[v]
            todo.append(next_v)
        # 同じ深さなら加算
        elif dist[next_v] == dist[v] + 1:
            cnt[next_v] += cnt[v]
            cnt[next_v] %= mod
print(cnt[-1] % mod)
