from collections import deque
from math import inf
import sys


def input(): return sys.stdin.readline().rstrip()


def main():
    def li(): return list(map(int, input().split()))
    def mi(): return map(int, input().split())
    def ii(): return int(input())

    N, M = mi()
    E = [li() for _ in range(M)]
    S, T = mi()
    S -= 1
    T -= 1

    G = [set() for _ in range(N)]
    for u, v in E:
        u -= 1
        v -= 1
        G[u].add(v)

    dist = [[inf] * 3 for _ in range(N)]

    todo = deque([(0, 0, S)])
    while todo:
        d, jmp, v = todo.popleft()
        if dist[v][jmp] <= d:
            continue

        dist[v][jmp] = d
        njmp = (jmp + 1) % 3
        for nv in G[v]:
            if dist[nv][njmp] <= d + 1:
                continue
            todo.append((d + 1, njmp, nv))

    print(dist[T][0] // 3 if dist[T][0] < inf else -1)


if __name__ == '__main__':
    main()
