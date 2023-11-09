H, W, M = map(int, input().split())
BOM = list(tuple(map(lambda x: int(x) - 1, input().split())) for _ in range(M))
ans = 0

Hs = [0] * H
Ws = [0] * W

for h, w in BOM:
    Hs[h] += 1
    Ws[w] += 1

BOM = set(BOM)

Wmax = max(Ws)
W_maxes = set(i for i, v in enumerate(Ws) if v == Wmax)
H_relates = set(h for h, w in BOM if w in W_maxes)

for h in range(H):
    _m = Hs[h] + Wmax
    if h in H_relates and all((h, w) in BOM for w in W_maxes):
        _m -= 1
    ans = max(_m, ans)

print(ans)
