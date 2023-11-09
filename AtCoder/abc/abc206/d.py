from collections import Counter

N = int(input())
A = list(map(int, input().split()))
uf = UnionFind(max(A) + 1)
for i in range(N // 2):
    if A[i] != A[-1 - i]:
        uf.union(A[i], A[-1 - i])
roots = uf.roots()
ans = 0
for p in roots:
    ans += uf.size(p) - 1
print(ans)
# print(roots)
