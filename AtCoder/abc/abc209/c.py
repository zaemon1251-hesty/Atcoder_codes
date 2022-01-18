mod = 10**9 + 7
N = int(input())
C = list(map(int, input().split()))
C = sorted(C)
t = 0
ans = 1
for i in range(N):
    ans *= max(0, C[i] - i)
    ans %= mod
print(ans)
