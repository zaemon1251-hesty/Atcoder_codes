N, M = map(int, input().split())
S = [input() for _ in range(N)]

inf = 1 << 60
DPl = [inf] * N
DPr = [inf] * N
DPl[0] = DPr[-1] = 0
for n in range(N):
    for d, s in enumerate(S[n]):
        if s == "1" and DPl[n] < inf:
            DPl[n + d + 1] = min(DPl[n + d + 1], DPl[n] + 1)

for n in range(N - 1, -1, -1):
    for d, s in enumerate(S[n]):
        if s == "1" and DPr[n + d + 1] < inf:
            DPr[n] = min(DPr[n], DPr[n + d + 1] + 1)

ans = [inf] * N
for c in range(N):
    for d in range(M):
        if S[c][d] == "0":
            continue
        #print(c, c + d + 1)
        v = DPl[c] + DPr[c + d + 1] + 1
        for x in range(c + 1, c + d + 1):
            ans[x] = min(ans[x], v)

ans = [v if v < inf else -1 for v in ans]
print(*ans[1:N - 1])
