from collections import deque
from heapq import heappop, heappush


def main():
    N, M, X, Y = map(int, input().split())
    inf = 1 << 60
    X -= 1
    Y -= 1
    G = [[]for _ in range(N)]
    dist = [inf] * N
    E = [list(map(int, input().split())) for _ in range(M)]
    E = list(set(E))
    for i in range(M):
        E[i][0] -= 1
        E[i][1] -= 1
        a, b, _, _ = E[i]
        G[a].append(i)
        G[b].append(i)
    todo = [(0, X)]
    dist[X] = 0
    while todo:
        now, v = heappop(todo)
        for i in G[v]:
            nv = E[i][1 - E[i].index(v)]
            t, k = E[i][2], E[i][3]
            wait = k - now % k
            wait = wait if wait != k else 0
            if dist[nv] <= now + t + wait:
                continue
            dist[nv] = now + t + wait
            heappush(todo, (dist[nv], nv))
    print(dist[Y] if dist[Y] < inf else -1)


if __name__ == '__main__':
    main()
