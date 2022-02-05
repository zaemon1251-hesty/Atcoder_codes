N = int(input())
s = len(str(N))-1
mod = 998244353
if N < 10:
    print(N * (N+1)//2)
    exit()
ans = 0
ans += 45
for i in range(1, s):
    z = pow(10, i, mod)
    ans += z * 9 * (z * 9 + 1) // 2
    ans %= mod

p = N - pow(10, s, mod) + 1
p %= mod
ans += p*(p+1)//2
print(ans % mod)
