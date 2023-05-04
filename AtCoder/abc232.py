def maina():
    a, b = map(int, input().split("x"))
    print(a * b)


def mainb():
    S = list(input())
    T = list(input())
    mod = 26
    for i in range(mod):
        S = [chr((ord(S[t]) - ord("a") + mod - 1) % mod + ord("a"))
             for t in range(len(S))]
        if S == T:
            print("Yes")
            return
    print("No")


def mainc():
    from itertools import permutations
    N, M = map(int, input().split())
    T = [tuple(map(lambda x:int(x) - 1, input().split())) for _ in range(M)]
    A = set(tuple(map(lambda x: int(x) - 1, input().split()))
            for _ in range(M))
    for P in permutations(range(N), N):
        flg = True
        for i, j in T:
            mi = min(P[i], P[j])
            Mj = max(P[i], P[j])
            if not (mi, Mj) in A:
                flg = False
                break
        if flg:
            print("Yes")
            return
    print("No")


def maind():
    inf = float("inf")
    from collections import deque
    h, w = map(int, input().split())
    grid = [list(input()) for _ in range(h)]
    dist = [[inf] * w for _ in range(h)]
    dist[0][0] = 0
    s = (0, 0)
    dx = [(1, 0), (0, 1)]
    todo = deque([s])
    d = 1
    while todo:
        qq = []
        for x, y in todo:
            for i in range(2):
                nx, ny = x+dx[i][0], y+dx[i][1]
                if nx < 0 or nx >= h or ny < 0 or ny >= w:
                    continue
                if dist[nx][ny] < inf:
                    continue
                if grid[nx][ny] == '#':
                    continue
                dist[nx][ny] = d
                qq.append((nx, ny))
        todo = qq
        d += 1
    print(d - 1)


def maine():
    MOD = 998244353
    H, W, K = map(int, input().split())
    x1, y1, x2, y2 = map(int, input().split())
    dp = [0]*4  # (x2,y2),(x2,any),(any,y2),(any,any)
    if x1 == x2 and y1 == y2:
        dp[0] = 1
    elif x1 == x2:
        dp[1] = 1
    elif y1 == y2:
        dp[2] = 1
    else:
        dp[3] = 1
    for _ in range(K):
        nexts = [
            (dp[1]+dp[2]) % MOD,
            (dp[0]*(W-1) % MOD+dp[1]*(W-2) % MOD+dp[3]) % MOD,
            (dp[0]*(H-1) % MOD+dp[2]*(H-2) % MOD+dp[3]) % MOD,
            (dp[1]*(H-1)+dp[2]*(W-1)+dp[3]*(H+W-4)) % MOD
        ]
        dp = nexts
    print(dp[0])


maine()
