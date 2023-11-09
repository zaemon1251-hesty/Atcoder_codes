N, M, X = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]
ans = 1 << 60

for i in range(1 << N):
    p = [0] * M
    cost = 0
    for j in range(N):
        if i >> j & 1:
            cost += A[j][0]
            for k in range(M):
                p[k] += A[j][k + 1]
    if all(alg >= X for alg in p):
        ans = min(ans, cost)
print(ans if ans < 1 << 60 else -1)
