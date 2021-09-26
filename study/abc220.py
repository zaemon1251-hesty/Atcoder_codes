def maina():
    a, b, c = map(int, input().split())
    for i in range(a, b+1):
        if i % c == 0:
            print(i)
            exit()
    else:
        print(-1)


def mainb():
    k = int(input())
    a, b = map(str, input().split())
    ap = 0
    bp = 0
    a = a[::-1]
    b = b[::-1]
    for i in range(len(a)):
        ap += int(a[i])*pow(k, i)
    for i in range(len(b)):
        bp += int(b[i])*pow(k, i)
    print(bp*ap)


def mainc():
    N = int(input())
    a = list(map(int, input().split()))
    X = int(input())
    s = sum(a)
    k = N*(X//s)
    r = X % s
    i = 0
    while r >= 0:
        r -= a[i]
        k += 1
        i += 1
    print(min(k, pow(10, 100)))


def maind():
    mod = 998244353
    N = int(input())
    a = list(map(int, input().split()))

    dp = [[0]*10 for _ in range(N)]
    dp[0][a[0]] += 1
    for i in range(1, N):
        y = a[i]
        for x in range(10):
            dp[i][(x+y) % 10] += dp[i-1][x]
            dp[i][(x*y) % 10] += dp[i-1][x]
            dp[i][(x+y) % 10] %= mod
            dp[i][(x*y) % 10] %= mod
    for i in range(10):
        dp[-1][i] %= mod
    print(*dp[-1], sep="\n")


def maine():
    mod = 998244353
    N, D = map(int, input().split())
    ans = 0
    for d in range(N):
        if d <= N-1-D:
            ans += pow(2, D+d, mod)*2
        if 0 < 2*(N-1-d)-D+1 < D:
            ans += (2*(N-1-d)-D+1)*pow(2, D-2+d, mod)*2
        ans %= mod

    print(ans % mod)


maine()
