N, M = map(int, input().split())
H = list(map(int, input().split()))
E = [list(map(int, input().split())) for _ in range(M)]
G = [set() for _ in range(N)]
ans = 0
for a, b in E:
    G[a-1].add(H[b-1])
    G[b-1].add(H[a-1])

for i in range(N):
    if not G[i] or H[i] > max(G[i]):
        ans += 1
print(ans)
