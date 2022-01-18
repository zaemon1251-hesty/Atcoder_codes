n, m = map(int, input().split())
G = [[]for i in range(n)]
for i in range(m):
    n1, k1 = map(int, input().split())
    G[n1 - 1].append(k1 - 1)
ans = 0
for i in range(n):
    ans += find(G,n,i)
print(ans)
