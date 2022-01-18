from collections import deque
N = int(input())
edge = [[]for i in range(N+1)]
weight = [[]for i in range(N+1)]
for i in range(1,N):
    u,v,w = map(int,input().split())
    edge[u].append(v)
    edge[v].append(u)
    weight[u].append(w)
    weight[v].append(w)
dist = [-1]*(N+1)
dist[1] = 0
que = deque([1])
while que:
    now = que.popleft()
    for i in range(len(edge[now])):
        nex = edge[now][i]
        if dist[nex] == -1:
            dist[nex] = dist[now]^weight[now][i]
            que.append(nex)
mod = int(1e9+7)
ans = 0
for i in range(60):
    cnt = [0]*2
    for j in range(N):
        cnt[dist[j+1]>>i&1] += 1
    ans += (1<<i)*cnt[0]*cnt[1]
    ans %= mod
print(ans)
_name__ == "__main__":
mainE()