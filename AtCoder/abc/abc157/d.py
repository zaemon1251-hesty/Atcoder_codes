N, M, K = map(int, input().split())
AB = [list(map(int, input().split())) for _ in range(M)]
CD = [list(map(int, input().split())) for _ in range(K)]
uf = UnionFind(N)
friend = [0]*N
blocked = [0]*N
for a, b in AB:
    uf.union(a-1, b-1)
    friend[a-1] += 1
    friend[b-1] += 1
for c, d in CD:
    if uf.same(d-1, c-1):
        blocked[c-1] += 1
        blocked[d-1] += 1
ans = [uf.size(i)-friend[i]-blocked[i]-1 for i in range(N)]
print(' '.join(map(str, ans)))
