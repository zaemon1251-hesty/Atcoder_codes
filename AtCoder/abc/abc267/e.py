from heapq import heappop, heappush


def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    aj = [0] * N
    E = [list(map(int, input().split())) for _ in range(M)]
    G = [set() for _ in range(N)]
    for u, v in E:
        u -= 1
        v -= 1
        G[u].add(v)
        G[v].add(u)

    deleted = set()
    todo = []
    for v in range(N):
        adjacency = sum(A[nv] for nv in G[v])
        aj[v] = adjacency
        heappush(todo, (adjacency, v))

    ans = 0
    cnt = 0
    while cnt < N and todo:
        deg, v = heappop(todo)
        if v in deleted:
            continue
        ans = max(ans, deg)

        deleted.add(v)
        for nv in G[v]:
            if nv not in deleted:
                aj[nv] -= A[v]
                heappush(todo, (aj[nv], nv))
    print(ans)


if __name__ == "__main__":
    main()
