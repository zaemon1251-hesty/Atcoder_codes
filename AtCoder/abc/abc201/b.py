<<<<<<< HEAD
def main():
    N = int(input())
    A = [list(map(str, input().split()))for _ in range(N)]
    A.sort(key=lambda x: int(x[1]), reverse=True)
    print(A[1][0])


if __name__ == '__main__':
    main()
=======
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
>>>>>>> f9ad35ec977c779c25cb6b4ce6092c52d1b94ee0
