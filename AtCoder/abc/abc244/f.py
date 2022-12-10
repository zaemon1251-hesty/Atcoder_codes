from collections import deque


def main():
    N, M = map(int, input().split())
    G = [[] for _ in range(N)]
    inf = 1 << 60
    E = [list(map(lambda x: int(x) - 1, input().split())) for _ in range(M)]
    for u, v in E:
        G[u].append(v)
        G[v].append(u)
    # dist[i][j] = {(i = s1s2...sN | si = {0,1} | si = [iが奇数回含まれているか]) && (j = 1..N
    # [j = 最後尾の頂点])} の時の最短パス長
    dist = [[inf] * N for _ in range(1 << N)]
    todo = deque([])
    for j in range(N):
        dist[0][j] = 0
        dist[1 << j][j] = 1
        todo.append((1 << j, j))
    while todo:
        s, u = todo.popleft()
        for nv in G[u]:
            if dist[s ^ (1 << nv)][nv] <= dist[s][u] + 1:
                continue
            dist[s ^ (1 << nv)][nv] = dist[s][u] + 1
            todo.append((s ^ (1 << nv), nv))
    ans = sum(min(dist[i]) for i in range(1 << N))
    print(ans)


if __name__ == '__main__':
    main()
