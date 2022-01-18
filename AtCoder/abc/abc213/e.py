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
_name__ == "__main__":
mori = 21
# maina()
# mainb()
# mainc()
# maind()
# maine()
# mainf()
