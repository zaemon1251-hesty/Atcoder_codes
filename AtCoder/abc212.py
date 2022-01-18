def mainc():
    from bisect import bisect
    N, M = map(int, input().split())
    A = sorted(list(map(int, input().split())))
    B = sorted(list(map(int, input().split())))
    ans = 10**9
    for i in range(N):
        tg = A[i]
        idx = bisect(B, A[i])
        ans = min(ans, abs(tg - B[min(idx, M-1)]),
                  abs(tg - B[max(0, idx - 1)]))
    print(ans)


def maind():
    from heapq import heappop, heappush
    Q = int(input())
    B = []
    num = 0
    for _ in range(Q):
        d = input()
        if len(d) != 1:
            ty, x = map(int, d.split())
            if ty == 1:
                heappush(B, x-num)
            else:
                num += x
        else:
            p = heappop(B)
            print(p + num)


def maine():
    mod = 998244353
    N, M, K = map(int, input().split())
    G = [[]for _ in range(N)]
    P = []
    dp = [0]*N
    dp[0] = 1
    for _ in range(M):
        u, v = map(int, input().split())
        u -= 1
        v -= 1
        G[u].append(v)
        G[v].append(u)
        P.append((u, v))
    for i in range(K):
        tmp = [sum(dp) % mod]*N
        for i in range(N):
            tmp[i] -= dp[i]
        for u, v in P:
            tmp[u] -= dp[v]
            tmp[u] %= mod
            tmp[v] -= dp[u]
            tmp[u] %= mod
        dp = tmp
    print(dp[0] % mod)


maine()
