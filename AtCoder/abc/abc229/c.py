N, W = map(int, input().split())
S = []
for _ in range(N):
    a, b = map(int, input().split())
    S.append([a, b])
S.sort(key=lambda x: x[0], reverse=True)
i = 0
ans = 0
while W and i < N:
    t = min(S[i][1], W)
    ans += S[i][0] * t
    W -= t
    i += 1
print(ans)
