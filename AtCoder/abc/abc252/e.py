from heapq import heapify, heappop, heappush
inf = 1 << 60


def main():
    N, M = map(int, input().split())
    G = [[] for _ in range(N)]
    E = {}
    for i in range(M):
        a, b, c = map(int, input().split())
        a -= 1
        b -= 1
        E[a, b] = i + 1
        E[b, a] = i + 1
        G[a].append((b, c))
        G[b].append((a, c))

    dist = [inf] * N
    que = [(0, 0, -1)]
    dist[0] = 0
    heapify(que)

    ans = []
    while que:
        cv, v, pv = heappop(que)

        if dist[v] < cv:
            continue
        if pv != -1:
            ans.append(E[v, pv])

        for nv, c in G[v]:
            if dist[nv] > dist[v] + c:
                dist[nv] = dist[v] + c
                heappush(que, (dist[nv], nv, v))

        if len(ans) == N - 1:
            print(*ans)
            exit()

    print(*ans)


if __name__ == '__main__':
    main()
