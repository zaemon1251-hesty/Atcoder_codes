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
