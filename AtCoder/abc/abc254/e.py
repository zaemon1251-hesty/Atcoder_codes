from collections import defaultdict


def main():
    N, M = map(int, input().split())
    G = [[] for _ in range(N)]
    dists = [defaultdict(lambda: N) for _ in range(N)]

    for i in range(M):
        a, b = map(int, input().split())
        G[a - 1].append(b - 1)
        G[b - 1].append(a - 1)

    for v in range(N):
        for nv in G[v]:
            for nvv in G[nv]:
                if nvv == v:
                    continue
                for nv3 in G[nvv]:
                    if nv3 == nv:
                        continue
                    dists[v][nv3] = min(dists[v][nv3], 3)
                dists[v][nvv] = min(dists[v][nvv], 2)
            dists[v][nv] = min(dists[v][nv], 1)
        dists[v][v] = 0

    Q = int(input())
    for _ in range(Q):
        x, k = map(int, input().split())
        print(sum(i + 1 for i, d in dists[x - 1].items() if d <= k))


if __name__ == "__main__":
    main()
