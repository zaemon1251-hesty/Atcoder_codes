from collections import deque
from collections import defaultdict
import sys


def maina():
    n = int(input())
    a = list(map(int, input().split()))
    b = sorted(a)
    for i in range(n):
        if a[i] == b[-2]:
            print(i + 1)
            exit()


def mainb():
    n = int(input())
    a = list(map(int, input().split()))
    a = sorted(a)
    print(a[1])


def mainc():
    # 座標圧縮
    h, w, n = map(int, input().split())
    x = []
    y = []
    z = []
    for i in range(n):
        a, b = map(int, input().split())
        x.append([a, i])
        y.append([b, i])
        z.append([a, b])

    ans = [[-1, -1] for _ in range(n)]
    x.sort(key=lambda x: x[0])
    y.sort(key=lambda x: x[0])
    cntx = 1
    cnty = 1
    px = x[0][0]
    py = y[0][0]
    for j in range(n):
        xx, s = x[j]
        yy, t = y[j]
        if xx > px:
            cntx += 1
            px = xx
        if yy > py:
            cnty += 1
            py = yy
        ans[s][0] = cntx
        ans[t][1] = cnty

    for item in ans:
        print(item[0], item[1])


def maind():

    sys.setrecursionlimit(10**6)

    n = int(input())
    G = [[] for _ in range(n)]
    for i in range(n-1):
        a, b = map(lambda x: int(x)-1, input().split())
        G[a].append(b)
        G[b].append(a)

    seen = [False]*n
    ans = []
    fl = False

    def dfs(G, v):
        if v == 0 and fl:
            return
        seen[v] = True
        ans.append(v + 1)

        for next_v in sorted(G[v]):
            if seen[next_v] == True:
                continue
            dfs(G, next_v)
            if ans[-1] != v + 1:
                ans.append(v + 1)
            fl = True

        if ans[-1] != v + 1:
            ans.append(v + 1)
    dfs(G, 0)
    print(*ans, sep=" ")


def maine():
    inf = 1 << 60

    def grid01BFS(G):
        """
        道と壁があって、上下左右に移動できるグリッドグラフにおいて、
        スタートからゴールまでの最小パンチ回数を求める
        """
        h, w = len(G), len(G[0])
        s = [0, 0]
        g = [h-1, w-1]
        dx = [0, 1, -1, 0]
        dy = [1, 0, 0, -1]
        dist = [[inf]*(w) for _ in range(h)]
        d = 1

        todo = deque([])
        todo.appendleft(s)
        dist[s[0]][s[1]] = 0
        while todo:
            x, y = todo.popleft()
            if x == g[0] and y == g[1]:
                break
            for i in range(4):
                nx, ny = x+dx[i], y+dy[i]
                # 0-indexで考える
                if nx < 0 or nx >= h or ny < 0 or ny >= w:
                    continue
                if G[nx][ny] == '#':
                    continue
                if dist[nx][ny] <= dist[x][y]:
                    continue
                dist[nx][ny] = dist[x][y]
                todo.appendleft([nx, ny])
            for i in range(-2, 3):
                for j in range(-2, 3):
                    if (i == -2 and j == -2) or (i == 2 and j == -2) or (i == -2 and j == 2) or (i == 2 and j == 2):
                        continue
                    nx, ny = x+i, y+j
                    # 0-indexで考える
                    if nx < 0 or nx >= h or ny < 0 or ny >= w:
                        continue
                    if dist[nx][ny] <= dist[x][y] + 1:
                        continue
                    dist[nx][ny] = dist[x][y] + 1
                    todo.append([nx, ny])
        return dist

    # ABC 184-E Third Avenue
    # 幅優先探索
    h, w = map(int, input().split())
    dist = [[inf]*w for _ in range(h)]
    grid = []
    for i in range(h):
        x = list(input())
        grid.append(x)

    dist = grid01BFS(grid)
    print(dist[-1][-1])


if __name__ == "__main__":
    mori = 21
    # maina()
    # mainb()
    # mainc()
    # maind()
    # maine()
    # mainf()
