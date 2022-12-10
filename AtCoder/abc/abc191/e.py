from collections import deque
import sys
from heapq import heappop, heappush
input = sys.stdin.readline


def main():
    N, M = map(int, input().split())
    G = [[] for _ in range(N)]
    inf = 1 << 60
    ans = []
    for _ in range(M):
        a, b, c = map(int, input().split())
        a -= 1
        b -= 1
        G[a].append((b, c))
    for i in range(N):
        dist = [inf] * N
        s = i
        dist[s] = 0
        tmp = inf
        todo = [(dist[s], s)]
        while todo:
            _, x = heappop(todo)
            for nx, c in G[x]:
                if nx == s:
                    tmp = min(tmp, dist[x] + c)
                    continue
                if dist[x] + c >= dist[nx]:
                    continue
                dist[nx] = dist[x] + c
                heappush(todo, (dist[nx], nx))
        ans.append(tmp if tmp < inf else -1)
    print(*ans, sep="\n")


if __name__ == '__main__':
    main()
