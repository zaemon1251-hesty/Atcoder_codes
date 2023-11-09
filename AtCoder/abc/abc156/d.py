n, a, b = map(int, input().split())
mod = 10**9 + 7


def cmb(n, r):
    r = min(n - r, r)  # nCrでもnCn-rでも一緒のことなので小さい方を取ることで高速化を図る
    a = 1
    b = 1
    for k in range(r):
        a *= n - r + 1 + k
        a %= mod
        b *= k + 1
        b %= mod
    return a * pow(b, mod - 2, mod) % mod


print((pow(2, n, mod) - 1 - cmb(n, a) - cmb(n, b)) % mod)
