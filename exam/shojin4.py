import sys


def input():
    return sys.stdin.readline().rstrip()


def arc074_a():
    def li():
        return list(map(int, input().split()))

    def mi():
        return map(int, input().split())

    def ii():
        return int(input())

    H, W = mi()
    ans = 1 << 60
    for h in range(1, H + 1):
        b = h * W
        c2, d2 = ((H - h) // 2) * W, (H - h) * (W // 2)
        c3, d3 = H * W - b - c2, H * W - b - d2
        ans = min(ans, max(b, c2, c3) - min(b, c2, c3))
        ans = min(ans, max(b, d2, d3) - min(b, d2, d3))

    H, W = W, H
    for h in range(1, H + 1):
        b = h * W
        c2, d2 = ((H - h) // 2) * W, (H - h) * (W // 2)
        c3, d3 = H * W - b - c2, H * W - b - d2
        ans = min(ans, max(b, c2, c3) - min(b, c2, c3))
        ans = min(ans, max(b, d2, d3) - min(b, d2, d3))

    print(ans)


def abc089_d():
    from itertools import product

    def li():
        return list(map(int, input().split()))

    def mi():
        return map(int, input().split())

    def ii():
        return int(input())

    H, W, D = mi()
    A = [li() for _ in range(H)]
    M = [[] for i in range(D)]
    for h, w in product(range(H), range(W)):
        M[A[h][w] % D].append((A[h][w], h, w))

    S = [[0] for i in range(D)]
    ref = {}
    for d in range(D):
        M[d].sort(key=lambda x: x[0])

        for i, (axy, x, y) in enumerate(M[d]):
            ref[axy] = i
            if i == len(M[d]) - 1:
                break
            _, u, v = M[d][i + 1]
            res = abs(x - u) + abs(y - v)
            S[d].append(S[d][-1] + res)

    Q = ii()
    que = [li() for _ in range(Q)]

    for s in range(Q):
        L, R = que[s]
        res = 0
        d = L % D
        src = ref[L]
        dst = ref[R]
        # print(M[d])
        # print(S[d])
        # print(d, src, dst)
        print(S[d][dst] - S[d][src])


def arc119_b():
    N = int(input())
    S = list(input())
    T = list(input())
    if S.count("1") != T.count("1"):
        print(-1)
        exit()

    z_s = [i for i in range(N) if S[i] == "0"]
    z_t = [i for i in range(N) if T[i] == "0"]

    print(sum(s != t for s, t in zip(z_s, z_t)))


if __name__ == '__main__':
    arc119_b()
