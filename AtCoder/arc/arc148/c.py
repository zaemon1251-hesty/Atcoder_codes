N, Q = map(int, input().split())
par = [-1, -1] + list(map(int, input().split()))
chd = [0] * (N + 1)
for i in range(2, N + 1):
    chd[par[i]] += 1
for _ in range(Q):
    __, *v = map(int, input().split())
    m = {*v}
    print(sum((chd[c] + (-1 if par[c] in m else 1) for c in v)))
