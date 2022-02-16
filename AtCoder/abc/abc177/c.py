N = int(input())
*A, = map(int, input().split())
MOD = 10**9+7
ans = 0
S = sum(A)

for i in range(N):
    S -= A[i]
    ans += A[i]*S
    ans %= MOD
print(ans)
