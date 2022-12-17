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


def abc096_d():
    def get_prime(n, get_sieve=False):
        prime = [False] * 2 + [True] * (n - 2)
        for i in range(2, n):
            if prime[i]:
                for j in range(i * 2, n, i):
                    prime[j] = False
        if get_sieve:
            return [i for i in range(2, n) if prime[i]]
        else:
            return prime

    def li():
        return list(map(int, input().split()))

    def mi():
        return map(int, input().split())

    def ii():
        return int(input())

    N = ii()
    primes = get_prime(55555, True)
    primes = [i for i in primes if i % 5 == 1]
    print(*primes[:N])


def arc106_c():
    N, M = map(int, input().split())

    if M == 0:
        i = 1
        cnt = 0
        while cnt < N:
            print(i, i + 1)
            i += 2
            cnt += 1
        return

    elif M < 0 or M >= N - 1:
        print(-1)
        return

    else:
        i = 2
        cnt = 0
        while cnt < M + 1:
            print(i, i + 1)
            i += 2
            cnt += 1

        i += 2
        print(1, i)
        cnt += 1

        i += 1
        while cnt < N:
            print(i, i + 1)
            cnt += 1
            i += 2


def agc003_b():
    N = int(input())
    A = [int(input()) for _ in range(N)]
    ans = 0

    breakpoints = set(i for i in range(N) if A[i] == 0)
    breakpoints.add(N)

    cur = 0
    for i in range(N + 1):
        if i in breakpoints:
            ans += cur // 2
            cur = 0
            continue
        cur += A[i]
    print(ans)


def abc070_d():
    import sys
    sys.setrecursionlimit(10**6)

    N = int(input())
    G = [[] for _ in range(N)]

    for _ in range(N - 1):
        a, b, c = map(int, input().split())
        a, b = a - 1, b - 1
        G[a].append((b, c))
        G[b].append((a, c))

    Q, K = map(int, input().split())
    K -= 1

    # Euler Tour Technique
    dist = [0] * N

    def dfs(v, p, d):
        for w, c in G[v]:
            if w == p:
                continue
            dist[w] = dist[v] + c
            dfs(w, v, d + 1)
    dist[K] == 0
    dfs(K, -1, 0)

    q = [list(map(int, input().split())) for _ in range(Q)]
    for x, y in q:
        x, y = x - 1, y - 1
        print(dist[x] + dist[y])


def agc014_b():
    def li():
        return list(map(int, input().split()))

    def mi():
        return map(int, input().split())

    def ii():
        return int(input())

    N, M = mi()
    E = [li() for _ in range(M)]
    cnt = [0] * N
    for a, b in E:
        cnt[a - 1] += 1
        cnt[b - 1] += 1

    if all(cn % 2 == 0 for cn in cnt):
        print("YES")
        return

    print("NO")


if __name__ == '__main__':
    agc014_b()
