def maina():
    s = input()
    if s[-1] == "r":
        print("er")
    else:
        print("ist")


def mainb():
    h, w = map(int, input().split())
    S = []
    for _ in range(h):
        S.append(list(map(int, input().split())))
    for i1 in range(h-1):
        for i2 in range(i1 + 1, h):
            for j1 in range(w-1):
                for j2 in range(j1 + 1, w):
                    if (S[i1][j1] + S[i2][j2]) > (S[i2][j1] + S[i1][j2]):
                        print('No')
                        exit()
    print("Yes")


mainb()


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


def maind():
    from collections import deque
    inf = 1 << 60
    M = int(input())
    G = [[]for _ in range(9)]
    for _ in range(M):
        x, y = map(lambda x: int(x) - 1, input().split())
        G[x].append(y)
        G[y].append(x)
    ans = dict()
    p = list(map(lambda x: int(x) - 1, input().split()))
    t = ['8']*9
    for i in range(8):
        t[p[i]] = str(i)
    t = ''.join(t)
    todo = deque([t])
    ans[t] = 0
    while todo:
        p = todo.popleft()
        w = p
        p = list(p)
        movable = p.index('8')
        for i in G[movable]:
            j = movable
            s = p.copy()
            s[i], s[j] = s[j], s[i]
            s = ''.join(s)
            if (s in ans):
                continue
            ans[s] = ans[w] + 1
            todo.append(s)
    print(ans['012345678'] if '012345678' in ans else -1)


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


mainb()
