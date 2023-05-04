<<<<<<< HEAD
from itertools import product

N = int(input())
K = int(input())
g = [list(input()) for _ in range(N)]

dr = [-1, 0, 1, 0]
dc = [0, -1, 0, 1]


def dfs(g):
    cnt = 0
    for i, j in product(range(N), repeat=2):
        if g[i][j] == 'o':
            cnt += 1
    if cnt == K:
        return 1

    res = 0
    for i, j in product(range(N), repeat=2):
        if g[i][j] != '.':
            continue
        if cnt > 0:
            ok = False
            for k in range(4):
                r = i + dr[k]
                c = j + dc[k]
                if not (0 <= r < N and 0 <= c < N):
                    continue
                if g[r][c] == 'o':
                    ok = True
            if not ok:
                continue

        g[i][j] = 'o'
        res += dfs(g)
        g[i][j] = '#'
        res += dfs(g)
        g[i][j] = '.'  # 戻す
        return res
    return res


ans = dfs(g)
print(ans)
=======
from math import gcd
N, M = map(int, input().split())
D = []
for i in range(M):
    a, c = map(int, input().split())
    D.append((a, c))
D.sort(key=lambda x: x[1])
ans = 0
X = N
#sdgs = N
for i in range(M):
    a, c = D[i][0], D[i][1]
    tmp = gcd(X, a)
    ans += c * (X - tmp)
    X = tmp
print(ans if X == 1 else -1)
_name__ == "__main__":
mori = 20
# maina()
# mainb()
# mainc()
maind()
# maine()
>>>>>>> f9ad35ec977c779c25cb6b4ce6092c52d1b94ee0
