from collections import deque


def main():
    N = int(input())
    edge = [[]for i in range(N + 1)]
    weight = [[]for i in range(N + 1)]
    for i in range(1, N):
        u, v, w = map(int, input().split())
        edge[u].append(v)
        edge[v].append(u)
        weight[u].append(w)
        weight[v].append(w)
    dist = [-1] * (N + 1)
    dist[1] = 0
    que = deque([1])
    while que:
        now = que.popleft()
        for i, nex in enumerate(edge[now]):
            if dist[nex] == -1:
                dist[nex] = dist[now] ^ weight[now][i]
                que.append(nex)
    mod = int(1e9 + 7)
    ans = 0
    for d in range(60):
        cnt = [0] * 2
        for j in range(N):
            cnt[dist[j + 1] >> d & 1] += 1
        ans += (1 << d) * cnt[0] * cnt[1]
        ans %= mod
    print(ans)


if __name__ == "__main__":
    main()
