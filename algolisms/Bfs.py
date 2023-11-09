from collections import deque

# from collections import defaultdict
# from collections import deque
inf = 1 << 60


def BFS(G, N, p):
    inf = 1 << 60
    dist = [inf] * N
    todo = deque([p])
    dist[p] = 0
    while todo:
        v = todo.popleft()
        # 何らかの処理
        for next_v in G[v]:
            if dist[next_v] != inf:
                continue
            # 何らかの処理
            todo.append(next_v)
    return dist


def gridBFS(G, s, g):
    """
    道と壁があって、上下左右に移動できるグリッドグラフについて、
    スタートからゴールの最小移動回数を求める
    """
    h, w = len(G), len(G[0])
    dx = [0, 1, -1, 0]
    dy = [1, 0, 0, -1]
    dist = [[0] * (w) for i in range(h)]
    seen = [[False] * (w) for i in range(h)]
    d = 1

    todo = set()
    todo.add(s)
    seen[s[0]][s[1]] = True
    while todo:
        qq = set()
        fl = True
        for x, y in todo:
            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]
                # 0-indexで考える
                if nx < 0 or nx >= h or ny < 0 or ny >= w:
                    continue
                if G[nx][ny] == "#":
                    continue
                if seen[nx][ny]:
                    continue
                seen[nx][ny] = True
                dist[nx][ny] = d
                qq.add((nx, ny))
                if nx == g[0] and ny == g[1]:
                    fl = False
                    break

            if not fl:
                break
        if not fl:
            break
        else:
            todo = qq
            d += 1
    # if dist[g[0]][g[1]] == inf:print(f"inf: {s}, {g}")
    return dist


def grid01BFS(G):
    """
    道と壁があって、上下左右に移動できるグリッドグラフにおいて、
    スタートからゴールまでの最小パンチ回数を求める
    """
    H, W = len(G), len(G[0])
    s = [0, 0]
    g = [H - 1, W - 1]
    dx = [0, 1, -1, 0]
    dy = [1, 0, 0, -1]
    dist = [[inf] * (W) for _ in range(H)]
    # d = 1

    todo = deque([])
    todo.appendleft(s)
    dist[s[0]][s[1]] = 0
    while todo:
        x, y = todo.popleft()
        if x == g[0] and y == g[1]:
            break
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            # 0-indexで考える
            if nx < 0 or nx >= H or ny < 0 or ny >= W:
                continue
            if G[nx][ny] == "#":
                continue
            if dist[nx][ny] <= dist[x][y]:
                continue
            dist[nx][ny] = dist[x][y]
            todo.appendleft([nx, ny])
        for i in range(-2, 3):
            for j in range(-2, 3):
                if (i == -2 and j == -2) or (i == 2 and j == -2) or (i == -2 and j == 2) or (i == 2 and j == 2):
                    continue
                nx, ny = x + i, y + j
                # 0-indexで考える
                if nx < 0 or nx >= h or ny < 0 or ny >= w:
                    continue
                if dist[nx][ny] <= dist[x][y] + 1:
                    continue
                dist[nx][ny] = dist[x][y] + 1
                todo.append([nx, ny])
    return dist
