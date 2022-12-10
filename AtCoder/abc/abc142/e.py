N, M = map(int, input().split())
inf = 2 << 60
C = []
for i in range(M):
    a, b = map(int, input().split())
    c = list(map(lambda x: int(x) - 1, input().split()))
    C.append((a, c))
dp = [inf for _ in range(1 << N)]
dp[0] = 0
for i in range(1 << N):
    for j in range(M):
        t = i
        a, c = C[j]
        for key in c:
            t = t | (1 << (key))
        dp[t] = min(dp[t], dp[i] + a)
print(dp[-1] if dp[-1] != inf else -1)
e()
