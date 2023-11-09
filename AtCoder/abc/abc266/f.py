from functools import lru_cache
import sys

input = sys.stdin.readline


def int2zidx(x):
    return int(x) - 1


def main():
    N = int(input())
    E = [list(map(int2zidx, input().split())) for _ in range(N)]
    G = [[] for _ in range(N)]
    divides = [-1] * N
    deg = [0] * N
    cycles = []
    Q = int(input())
    QUERIES = [list(map(int2zidx, input().split())) for _ in range(Q)]

    for u, v in E:
        G[u].append(v)
        G[v].append(u)
        deg[u] += 1
        deg[v] += 1

    # 閉路上の頂点を列挙
    que = [i for i in range(N) if deg[i] == 1]
    while que:
        v = que.pop()
        divides[v] = -2
        for nv in G[v]:
            if deg[nv] >= 2:
                deg[nv] -= 1
                if deg[nv] == 1:
                    que.append(nv)

    # 閉路上の頂点を根としてdfs
    cycles = [i for i in range(N) if divides[i] == -1]
    for sts in cycles:
        todo = [sts]
        while todo:
            v = todo.pop()
            for nv in G[v]:
                if divides[nv] == -2:
                    divides[nv] = sts
                    todo.append(nv)

    # print(cycles)
    # print(divides)
    for x, y in QUERIES:
        if (
            ((divides[x] == divides[y]) and (divides[x] != -1))
            or (divides[x] == -1 and divides[y] == x)
            or (divides[y] == -1 and divides[x] == y)
        ):
            print("Yes")
        else:
            print("No")


if __name__ == "__main__":
    main()
