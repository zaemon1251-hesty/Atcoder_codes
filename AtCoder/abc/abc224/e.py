from collections import defaultdict

h, w, n = map(int, input().split())
z = []
dpw = [0] * (w + 1)
dph = [0] * (h + 1)
ans = [0] * n
for i in range(n):
    a, b, p = map(int, input().split())
    z.append((a - 1, b - 1, p, i))
z.sort(key=lambda x: x[2], reverse=True)
lazh = defaultdict(int)
lazw = defaultdict(int)
for j in range(n):
    x, y, p, i = map(int, z[j])
    ans[i] = max(dph[x], dpw[y])
    lazh[x] = max(lazh[x], ans[i] + 1)
    lazw[y] = max(lazw[y], ans[i] + 1)
    if j < n - 1:
        if p > z[j + 1][2]:
            for k, v in lazh.items():
                dph[k] = max(v, dph[k])
            for k, v in lazw.items():
                dpw[k] = max(v, dpw[k])
            lazh = defaultdict(int)
            lazw = defaultdict(int)
print(*ans, sep="\n")
b()
