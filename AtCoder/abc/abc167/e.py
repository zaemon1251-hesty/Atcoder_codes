MOD = 998244353
n, m, k = map(int, input().split())
if m == 1:
    if k < n - 1:
        print(0)
    else:
        print(1)
    exit()


def factorial(n):
    fact = [1] * (n + 1)
    ifact = [0] * (n + 1)
    for i in range(1, n + 1):
        fact[i] = fact[i-1] * i % MOD
    ifact[n] = pow(fact[n], MOD - 2, MOD)
    for i in range(n, 0, -1):
        ifact[i-1] = ifact[i] * i % MOD
    return fact, ifact


fact, ifact = factorial(n)


def comb(n, r):
    if r < 0 or r > n:
        return 0
    return fact[n] * ifact[r] * ifact[n-r] % MOD


s = m * pow(m - 1, n - 1, MOD) % MOD
inv = pow(m - 1, MOD - 2, MOD)
ans = 0
for i in range(k + 1):
    ans += s * pow(inv, i, MOD) * comb(n - 1, i)
    ans %= MOD
print(ans % MOD)
