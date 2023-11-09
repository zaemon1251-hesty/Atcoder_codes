from copy import copy
from bisect import bisect_right, bisect_left

H, W, K = map(int, input().split())
G = [list(input()) for _ in range(H)]
inf = 1 << 60
ans = inf


def getWbag(sep):
    bg = {i: 0 for i in sep}
    wbag = 0
    bag = copy(bg)
    y = 0
    score = 0
    flg = False
    while y < W:
        for x in range(H):
            if G[x][y] == "1":
                idx = bisect_left(sep, x)
                t = sep[idx]
                bag[t] += 1
                if bag[t] > K:
                    if score == 1:
                        flg = True
                        break
                    wbag += 1
                    bag = copy(bg)
                    y -= 1
                    score = 1
                    break
        score = 0
        y += 1
        if flg:
            wbag = inf
            break
    return wbag


for i in range(1 << (H - 1)):
    sep = []
    for j in range(H - 1):
        if (i >> j) & 1:
            sep.append(j)
    sep.append(H - 1)
    ans = min(ans, getWbag(sep) + len(sep) - 1)
print(ans)
e()
