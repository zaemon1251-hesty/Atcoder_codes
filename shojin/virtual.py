def abc258_b():
    from itertools import product

    def li():
        return list(map(int, input().split()))

    def mi():
        return map(int, input().split())

    def ii():
        return int(input())

    N = ii()
    A = [list(input()) for _ in range(N)]
    ans = []

    direc_8 = [(1, 0), (0, 1), (-1, 0), (0, -1),
               (1, -1), (-1, 1), (1, 1), (-1, -1)]
    ans = 0
    for i, j in product(range(N), repeat=2):
        for d in range(8):
            tmp = []
            dx, dy = direc_8[d]
            for rep in range(N):
                tmp.append(A[(i + dx * rep) % N][(j + dy * rep) % N])
            res = int("".join(map(str, tmp)))
            ans = max(ans, res)

    print(ans)


def arc079_a():
    from heapq import heappop, heappush

    def li():
        return list(map(int, input().split()))

    def mi():
        return map(int, input().split())

    def ii():
        return int(input())

    N, M = mi()

    G = [[] for _ in range(N)]

    for _ in range(M):
        a, b = mi()
        a -= 1
        b -= 1
        G[a].append(b)
        G[b].append(a)
    inf = 1 << 32
    dist = [inf] * N
    dist[0] = 0
    todo = [0]
    while todo:
        v = heappop(todo)
        for nv in G[v]:
            if dist[nv] > dist[v] + 1:
                dist[nv] = dist[v] + 1
                heappush(todo, nv)
    print("POSSIBLE" if dist[N - 1] == 2 else "IMPOSSIBLE")


def agc023_a():
    def li():
        return list(map(int, input().split()))

    def mi():
        return map(int, input().split())

    def ii():
        return int(input())

    N = ii()
    A = li()
    for s in range(1 << N):
        if sum(A[i] for i in range(N))


def abc278_e():
    def li():
        return list(map(int, input().split()))

    def mi():
        return map(int, input().split())

    def ii():
        return int(input())
    H, W, N, h, w = mi()
    A = [list(map(lambda x:x - 1, li()))for _ in range(H)]
    Colors = [0] * N

    S = [[[0] * N for _ in range(W + 1)] for _ in range(H + 1)]
    for i in range(H):
        for j in range(W):
            Colors[A[i][j]] += 1
            for k in range(N):
                S[i + 1][j + 1][k] += S[i + 1][j][k] + \
                    S[i][j + 1][k] - S[i][j][k] + (A[i][j] == k)

    ans = [[0] * (W - w + 1) for _ in range(H - h + 1)]

    for i in range(H - h + 1):
        for j in range(W - w + 1):
            res = 0
            for k in range(N):
                res += (
                    S[i + h][j + w][k] -
                    S[i][j + w][k] -
                    S[i + h][j][k] +
                    S[i][j][k]
                ) != Colors[k]
            ans[i][j] = res

    for a in ans:
        print(*a)


if __name__ == "__main__":
    abc278_e()
