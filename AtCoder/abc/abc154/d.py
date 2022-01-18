N, K = map(int, input().split())
P = list(map(lambda x: (int(x) * (int(x) + 1) // 2) / int(x), input().split()))
tmp = sum(P[:K])
ans = tmp
for i in range(N - K):
    tmp += P[K + i] - P[i]
    ans = max(ans, tmp)
print(ans)
