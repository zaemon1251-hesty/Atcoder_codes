N = int(input())
S = []
ans = 0
for _ in range(N):
    x, y = map(int, input().split())
    S.append([x, y])
for i in range(N - 2):
    x1, y1 = S[i][0], S[i][1]
    for j in range(i + 1, N - 1):
        x2, y2 = S[j][0], S[j][1]
        for k in range(j + 1, N):
            x3, y3 = S[k][0], S[k][1]
            ans += (x2 - x1) * (y3 - y1) - (x3 - x1) * (y2 - y1) != 0
print(ans)
