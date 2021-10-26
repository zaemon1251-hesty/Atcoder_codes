def mainc():
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


def maine():
    from collections import defaultdict
    h, w, n = map(int, input().split())
    z = []
    dpw = [0]*(w+1)
    dph = [0]*(h+1)
    ans = [0]*n
    for i in range(n):
        a, b, p = map(int, input().split())
        z.append((a-1, b-1, p, i))
    z.sort(key=lambda x: x[2], reverse=True)
    lazh = defaultdict(int)
    lazw = defaultdict(int)
    for j in range(n):
        x, y, p, i = map(int, z[j])
        ans[i] = max(dph[x], dpw[y])
        lazh[x] = max(lazh[x], ans[i] + 1)
        lazw[y] = max(lazw[y], ans[i] + 1)
        if j < n-1:
            if p > z[j+1][2]:
                for k, v in lazh.items():
                    dph[k] = max(v, dph[k])
                for k, v in lazw.items():
                    dpw[k] = max(v, dpw[k])
                lazh = defaultdict(int)
                lazw = defaultdict(int)

    print(*ans, sep='\n')


maine()
