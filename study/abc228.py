def mainc():
    import bisect
    N, K = map(int, input().split())
    P = []
    S = []
    for i in range(N):
        t = sum(list(map(int, input().split())))
        P.append(t)
        S.append(t)
    S.sort()
    ans = []
    for i in range(N):
        a = P[i]
        idx = N - bisect.bisect_left(S, a + 301)
        ans.append('Yes' if K > idx else 'No')
    print(*ans, sep="\n")


def maind():
    def find(x):
        if P[x] < 0:
            return x
        P[x] = find(P[x])
        return P[x]

    def unite(x, y):
        x, y = find(x), find(y)
        if x != y:
            P[x] = y

    N = 1 << 20
    A, P = [-1]*N, [-1]*N
    for _ in range(int(input())):
        t, x = map(int, input().split())
        p = x % N
        if t == 1:
            p = find(p)
            A[p] = x
            unite(p, (p+1) % N)
        else:
            print(A[p])


def maine():
    mod = 998244353
    N, K, M = map(int, input().split())
    if M % mod == 0:
        print(0)
        exit()
    S = pow(K, N, mod-1)
    S %= mod - 1
    ans = pow(M, S, mod)
    print(ans)


if __name__ == "__main__":
    maine()
