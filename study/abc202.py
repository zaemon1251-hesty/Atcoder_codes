def cmb(n,r):
    r = min(n-r,r) #nCrでもnCn-rでも一緒のことなので小さい方を取ることで高速化を図る
    a = 1
    b = 1
    for k in range(r):
        a *= (n-r+1+k)

        b *= (k+1)

    return a // b


def maina():
    a,b,c = map(int, input().split())
    print(21 - a - b - c)


def mainb():
    s = list(input())
    ans = ''
    for i in s:
        if i == "9":
            ans = '6' + ans
        elif i == "6":
            ans = "9" + ans
        else:
            ans = i + ans
    print(ans)


def mainc():
    n = int(input())
    from collections import Counter
    from bisect import bisect_left, bisect_right
    A = sorted(list(map(int, input().split())))
    B = list(map(int, input().split()))
    C = Counter(list(map(lambda x:int(x) - 1, input().split())))
    ans = 0
    for k,v in C.items():
        val = B[k]
        ans += v * (bisect_right(A, val) - bisect_left(A, val))
    print(ans)


def maind():
    A, B, k = map(int, input().split())
    S = A + B
    ans = ""
    for i in range(S):
        if k == 1:
            for _ in range(A):
                ans += "a"
            for _ in range(B):
                ans += "b"
            print(ans)
            exit()
        s = cmb(A - 1 + B, A -1)
        if k <= s:
            ans += "a"
            A -= 1
        else:
            ans += "b"
            B -= 1
            k -= s
    print(ans)

#global変数の都合
t = 0
def maine():
    import sys
    import bisect
    sys.setrecursionlimit(10**6)


    N = int(input())
    P = list(map(int, input().split()))
    Q = int(input())

    C = [[] for _ in range(N)]
    for c, p in enumerate(P, 2):
        c -= 1
        p -= 1
        C[p].append(c)

    tin = [-1] * N
    tout = [-1] * N
    dist = [-1] * N
    dist[0] = 0
    depth = [[] for _ in range(N)]



    def dfs(now):
        global t
        tin[now] = t
        t += 1
        depth[dist[now]].append(tin[now])
        for to in C[now]:
            dist[to] = dist[now] + 1
            dfs(to)
        tout[now] = t
        t += 1

    dfs(0)

    for i in range(Q):
        u, d = map(int, input().split())
        u -= 1
        r = bisect.bisect_left(depth[d], tout[u])
        l = bisect.bisect_left(depth[d], tin[u])
        print(r - l)



if __name__ == '__main__':
    #maina()
    #mainb()
    #mainc()
    #maind()
    #maine()
    mori = True