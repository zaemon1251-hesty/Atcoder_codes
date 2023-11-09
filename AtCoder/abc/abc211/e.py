from itertools import product

N = int(input())
K = int(input())
g = [list(input()) for _ in range(N)]

dr = [-1, 0, 1, 0]
dc = [0, -1, 0, 1]


def dfs(g):
    cnt = 0
    for i, j in product(range(N), repeat=2):
        if g[i][j] == "o":
            cnt += 1
    if cnt == K:
        return 1

    res = 0
    for i, j in product(range(N), repeat=2):
        if g[i][j] != ".":
            continue
        if cnt > 0:
            ok = False
            for k in range(4):
                r = i + dr[k]
                c = j + dc[k]
                if not (0 <= r < N and 0 <= c < N):
                    continue
                if g[r][c] == "o":
                    ok = True
            if not ok:
                continue

        g[i][j] = "o"
        res += dfs(g)
        g[i][j] = "#"
        res += dfs(g)
        g[i][j] = "."  # 戻す
        return res
    return res


ans = dfs(g)
print(ans)
