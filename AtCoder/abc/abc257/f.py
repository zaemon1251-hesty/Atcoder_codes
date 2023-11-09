from collections import deque

inf = 1 << 60


def main():
    N, M = map(int, input().split())
    E = [list(map(lambda x: int(x) - 1, input().split())) for _ in range(M)]
    G = [[] for _ in range(N)]

    tels = set()
    for u, v in E:
        if u == -1:
            tels.add(v)
        else:
            G[u].append(v)
            G[v].append(u)

    dist_st, dist_en = [inf] * N, [inf] * N
    min_st, min_en = [inf], [inf]

    for dist, src, min_v in zip([dist_st, dist_en], [0, N - 1], [min_st, min_en]):
        dist[src] = 0
        todo = deque([src])
        while todo:
            v = todo.popleft()
            if v in tels:
                min_v[0] = min(dist[v], min_v[0])
            for nv in G[v]:
                if dist[nv] > dist[v] + 1:
                    dist[nv] = dist[v] + 1
                    todo.append(nv)

    min_st, min_en = *min_st, *min_en

    anses = []
    for i in range(N):
        ans = min(
            dist_st[N - 1],
            dist_st[i] + 1 + min_en,
            min_st + 1 + dist_en[i],
            min_st + 1 + 1 + min_en,
        )
        if ans == inf:
            ans = -1
        anses.append(ans)
    print(*anses)


if __name__ == "__main__":
    main()
