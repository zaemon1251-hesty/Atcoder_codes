N, M = map(int, input().split())
A = [0] * N
S = [tuple(map(lambda x: int(x) - 1, input().split())) for i in range(M)]
uf = UnionFind(N)
for i, j in S:
    if uf.same(i, j):
        print("No")
        exit()
    uf.union(i, j)
    A[i] += 1
    A[j] += 1
print("Yes" if max(A) <= 2 else "No")
