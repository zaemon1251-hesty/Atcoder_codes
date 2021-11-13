inf = 10 ** 20
#from collections import deque


def bfs(G, s):
    """
    道と壁があって、上下左右に移動できるグリッドグラフについて、
    スタートからゴールの最小移動回数を求める
    """
    h, w = len(G), len(G[0])
    dx = [0, 1, -1, 0]
    dy = [1, 0, 0, -1]
    dist = [[0]*(w) for i in range(h)]
    d = 1
    seen = [[False]*(w) for i in range(h)]
    seen[s[0]][s[1]] = True
    todo = []
    todo.append(s)
    while todo:
        qq = []
        for x, y in todo:
            for i in range(4):
                nx, ny = x+dx[i], y+dy[i]
                # 0-indexで考える
                if nx < 0 or nx >= h or ny < 0 or ny >= w:
                    continue
                if G[nx][ny] == '#':
                    continue
                if seen[nx][ny]:
                    continue
                seen[nx][ny] = True
                dist[nx][ny] = d
                qq.append((nx, ny))
        todo = qq
        d += 1

    return dist


def maina():
    s = input()
    print(chr(ord(s) + 1))


def mainb():
    n, k, m = map(int, input().split())
    A = list(map(int, input().split()))

    print(max(0, m * n - sum(A)) if m * n - sum(A) <= k else -1)


def mainc():
    n, m = map(int, input().split())
    p = [0] * n
    ans = 0
    ac = set()
    for i in range(m):
        q, s = map(str, input().split())
        q = int(q) - 1
        if s == "WA":
            p[q] += 1
        elif not q in ac:
            ac.add(q)
            ans += p[q]
    else:
        print(len(ac), ans)


def maind():
    H, W = map(int, input().split())
    G = [list(input()) for _ in range(H)]
    ans = 0

    for i in range(H):
        for j in range(W):
            if G[i][j] == "#":
                continue
            dists = bfs(G, (i, j))
            dmax = max(max(dist) for dist in dists)
            ans = max(ans, dmax)
    print(ans)


def maine():
    # cmb の逐次計算
    mod = 10**9 + 7

    def cmb(n, r):
        if n < r:
            return 0
        r = min(n-r, r)
        a = 1
        b = 1
        for k in range(r):
            a *= (n-r+1+k)
            a %= mod
            b *= (k+1)
            b %= mod
        return a * pow(b, mod-2, mod) % mod

    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    ans = 0
    # ll[i] = cmb(N-i-1,K-1)
    # rr[i] = cmb(i,K-1)
    ll = [cmb(N-1, K-1)]
    rr = [cmb(0, K-1)]
    for i in range(N-1):
        l = ll[-1]
        l *= (N-K-i)
        l *= pow(N-i-1, mod-2, mod)
        l %= mod
        if i == N-K:
            l = 0
        ll.append(l)
        r = rr[-1]
        r *= i+1
        r *= pow(i-K+2, mod-2, mod)
        r %= mod
        if i == K-2:
            r = 1
        rr.append(r)
    #print(ll, rr, sep="\n")
    for i in range(N):
        ans -= ll[i] * A[i]
        ans += rr[i] * A[i]
        ans %= mod
    print(ans % mod)


if __name__ == '__main__':
    # maina()
    # mainb()
    # mainc()
    # maind()
    maine()
