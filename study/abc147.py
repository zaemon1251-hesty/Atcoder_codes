def check(N, hon, X, Y):
    for i in range(N):
        if hon[i] == 0:
            continue
        for x, y in zip(X[i], Y[i]):
            if hon[x] != y:
                return False
    return True


def mainc():
    N = int(input())
    A = []
    X = []
    Y = []
    for _ in range(N):
        a = int(input())
        t_x = []
        t_y = []
        for t in range(a):
            x, y = map(int, input().split())
            x -= 1
            t_x.append(x)
            t_y.append(y)
        X.append(t_x)
        Y.append(t_y)
        A.append(a)

    ans = 0
    for i in range(1 << N):
        hon = [0]*N
        for j in range(N):
            if (i >> j) & 1:
                hon[j] = 1
        if check(N, hon, X, Y):
            ans = max(ans, sum(hon))
    print(ans)


def maind():
    mod = 10**9+7
    n = int(input())
    a = list(map(int, input().split()))
    d = [0]*60
    ans = 0
    for j in range(60):
        pr = 0
        ng = 0
        for i in range(n):
            if (a[i] >> j) & 1:
                pr += 1
            else:
                ng += 1
        ans += pr*ng*pow(2, j)
        ans %= mod

    print(ans % mod)


if __name__ == "__main__":
    # mainc()
    maind()
