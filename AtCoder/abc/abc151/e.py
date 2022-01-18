# cmb の逐次計算
mod = 10**9 + 7
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
N, K = map(int, input().split())
A = list(map(int, input().split()))
A.sort()
ans = 0
# ll[i] = cmb(N-i-1,K-1)
# rr[i] = cmb(i,K-1)
ll = [cmb(N-1, K-1)]
rr = [cmb(0, K-1)]
for i in range(N-1):
    l = ll[-1]
    l *= (N-K-i)
    l *= pow(N-i-1, mod-2, mod)
    l %= mod
    if i == N-K:
        l = 0
    ll.append(l)
    r = rr[-1]
    r *= i+1
    r *= pow(i-K+2, mod-2, mod)
    r %= mod
    if i == K-2:
        r = 1
    rr.append(r)
for i in range(N):
    ans -= ll[i] * A[i]
    ans += rr[i] * A[i]
    ans %= mod
print(ans % mod)
_name__ == '__main__':
# maina()
# mainb()
# mainc()
# maind()
maine()
