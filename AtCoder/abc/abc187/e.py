import sys
sys.setrecursionlimit(10**6)

# python の 再帰 では間に合わない


def main():
    N = int(input())
    E = [list(map(lambda x: int(x) - 1, input().split()))
         for _ in range(N - 1)]
    Q = int(input())
    Qs = [list(map(int, input().split())) for _ in range(Q)]

    c = [0] * N
    seen = [False] * N
    depth = [0] * N
    G = [[] for _ in range(N)]

    for a, b in E:
        G[a].append(b)
        G[b].append(a)

    def dfs(v, p, d):
        depth[v] = d
        for next_v in G[v]:
            if next_v == p:
                continue
            dfs(next_v, v, d + 1)

    def dfs_c(v, p, x):
        c[v] += x
        for next_v in G[v]:
            if next_v == p:
                continue
            dfs_c(next_v, v, c[v])
    # dfs(0, -1, 0)
    todo = [0]
    d = 0
    while todo:
        v = todo.pop()
        seen[v] = True
        for nv in G[v]:
            if seen[nv]:
                continue
            depth[nv] = depth[v] + 1
            todo.append(nv)

    for t, e, x in Qs:
        t -= 1
        e -= 1
        tg = E[e][t]
        op = E[e][1 - t]
        if depth[tg] > depth[op]:
            c[tg] += x
        else:
            c[0] += x
            c[op] -= x

    # dfs_c(0, -1, 0)

    todo = [0]
    while todo:
        v = todo.pop()
        for nv in G[v]:
            if depth[nv] < depth[v]:
                continue
            c[nv] += c[v]
            todo.append(nv)
        d += 1

    print(*c, sep="\n")


if __name__ == '__main__':
    main()
