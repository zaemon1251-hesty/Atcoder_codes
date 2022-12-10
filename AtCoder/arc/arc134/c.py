N, K = map(int, input().split())
*A,  = map(int, input().split())

mod = 998244353


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


ans = cmb(2 * A[0] - sum(A) - 1, K - 1)
for i in range(1, N):
    ans *= cmb(A[i] + K - 1, K - 1)
    ans %= mod
print(ans % mod)
