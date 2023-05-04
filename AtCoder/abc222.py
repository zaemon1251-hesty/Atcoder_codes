def maina():
    s = int(input())
    # return '%04d' % s)


def mainb():
    N, P = map(int, input().split())
    A = list(map(int, input().split()))
    # return sum([i < P for i in A]))


def mainc():
    def jd(a, b):
        if a == b:
            return 2
        elif a == "G":
            if b == "C":
                return 0
            elif b == "P":
                return 1
        elif a == "C":
            if b == "G":
                return 1
            elif b == "P":
                return 0
        elif a == "P":
            if b == "G":
                return 0
            elif b == "C":
                return 1

    N, M = map(int, input().split())
    A = []
    for i in range(2*N):
        t = list(input())
        A.append(t)
    rank = list(range(2*N))
    wins = [0]*2*N
    for j in range(M):
        t = [0]*2*N
        for k in range(N):
            a = A[rank[2*k]][j]
            b = A[rank[2*k+1]][j]
            res = jd(a, b)
            if (res == 2):
                pass
            elif (res == 1):
                wins[rank[2*k+1]] -= 1
            else:
                wins[rank[2*k]] -= 1
        rank = sorted(enumerate(wins), key=lambda x: (x[1], x[0]))
        tmp = []
        for item in rank:
            tmp.append(item[0])
        rank = tmp
    for i in rank:
        print(i+1)


def maind():
    mod = 998244353
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    R = [[0]*3010 for _ in range(N+1)]
    R[0][0] = 1
    A = [0] + A
    B = [0] + B
    for i in range(N+1):
        for j in range(3010):
            if A[i] <= j <= B[i] and i > 0:
                R[i][j] = R[i-1][j] + R[i][j-1]
            elif not (i == j == 0):
                R[i][j] = R[i][j-1]
            R[i][j] %= mod
    print(R[-1][-1] % mod)


def maine():
    import sys
    from collections import defaultdict
    sys.setrecursionlimit(10**6)
    mod = 998244353
    N, M, K = map(int, input().split())
    A = list(map(int, input().split()))
    E = [0]*(N-1)
    G = [[] for _ in range(N)]
    for i in range(N-1):
        u, v = map(int, input().split())
        u -= 1
        v -= 1
        G[u].append([v, i])
        G[v].append([u, i])

    for i in range(M-1):
        s = A[i]-1
        g = A[i+1]-1

        def dfs(G, v, p):
            if v == g:
                return True
            for next_v, e in G[v]:
                if next_v == p:
                    continue
                if dfs(G, next_v, v):
                    E[e] += 1
                    return True
            return False
        dfs(G, s, -1)

    S = sum(E)
    if (S + K) % 2 != 0 or S + K < 0 or S - K < 0:
        print(0)
        exit()
    R = min((S + K) // 2, (S - K) // 2)
    dp = [0 for _ in range(R + 1)]
    dp[0] = 1
    for v in E:
        if E == 0:
            continue
        for c in range(R, v-1, -1):
            dp[c] += dp[c-v]
            dp[c] %= mod
    print(dp[R] % mod)


maine()
