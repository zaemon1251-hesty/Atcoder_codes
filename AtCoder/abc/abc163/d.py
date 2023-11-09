N, K = map(int, input().split())
mod = 10**9 + 7
ans = 0
cr = sum(range(K))
ut = sum(range(N - K + 1, N + 1))
for i in range(K, N + 2):
    ans += ut - cr + 1
    ans %= mod
    cr += i
    ut += N - i
print(ans % mod)
