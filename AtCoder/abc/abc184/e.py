from collections import defaultdict, deque


def main():
    # ABC 184-E Third Avenue
    # 幅優先探索
    h, w = map(int, input().split())
    s = 0
    g = 0

    dic = defaultdict(list)

    grid = []
    for i in range(h):
        x = list(input())
        for j in range(w):
            if x[j] == "S":
                s = (i, j)
                x[j] = "."
            elif x[j] == "G":
                g = (i, j)
            elif x[j] != "." and x[j] != "#":
                dic[x[j]].append((i, j))
        grid.append(x)

    # テレポート名をセット型で保存
    alpha = set(dic.keys())
    inf = 10e7
    dx = [1, 0, 0, -1]
    dy = [0, 1, -1, 0]

    dist = [[inf] * (w) for i in range(h)]

    todo = deque([(s[0], s[1])])
    dist[s[0]][s[1]] = 0

    # dは最小移動回数（秒数）
    d = 1

    while todo:
        x, y = todo.popleft()
        # テレポート可能なら上下左右のほかに、テレポート先もqueueに入れる
        # 一度そのテレポート名のマスに来たら次から無視
        if grid[x][y] in alpha:
            kr = dic[grid[x][y]]
            for telx, tely in kr:
                if telx != x or tely != y:
                    if dist[telx][tely] == inf:
                        dist[telx][tely] = d
                        todo.append((telx, tely))
            alpha.discard(grid[x][y])
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            # 0-indexで考える
            if nx < 0 or nx >= h or ny < 0 or ny >= w:
                continue
            if grid[nx][ny] == "#":
                continue
            if dist[nx][ny] != inf:
                continue
            dist[nx][ny] = d
            todo.append((nx, ny))
            if grid[nx][ny] == "G":
                print(dist[nx][ny])
                exit()
        d += 1

    answer = dist[g[0]][g[1]]
    if answer != inf:
        print(answer)
    else:
        print(-1)


if __name__ == "__main__":
    main()
