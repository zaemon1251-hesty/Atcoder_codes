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
            nx, ny = x + dx[i][0], y + dx[i][1]
            if nx < 0 or nx >= h or ny < 0 or ny >= w:
                continue
            if dist[nx][ny] < inf:
                continue
            if grid[nx][ny] == "#":
                continue
            dist[nx][ny] = d
            qq.append((nx, ny))
    todo = qq
    d += 1
print(d - 1)
