def maind():
    mod = 10**9 + 7
    X, Y = map(int, input().split())
    z = X + Y
    if (X + Y) % 3 != 0 or not (z//3 <= X <= 2*z//3):
        print(0)
        exit()
    st = z//3
    u = X - st
    ans = 1
    lazy = 1
    for i in range(u):
        ans *= st - i
        lazy *= i + 1
        ans %= mod
        lazy %= mod
    ans *= pow(lazy, mod - 2, mod)
    print(ans % mod)


if __name__ == "__main__":
    maind()
