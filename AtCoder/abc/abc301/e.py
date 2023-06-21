from collections import deque

inf = 1 << 30

dxdy = [(-1, 0), (1, 0), (0, -1), (0, 1)]

h, w, t = map(int, input().split())
a = [input() for _ in range(h)]


def bfs(sx, sy):
    costs = [[inf] * w for _ in range(h)]
    costs[sx][sy] = 0
    todo = deque()
    todo.append((sx, sy))
    while todo:
        x, y = todo.popleft()
        for dx, dy in dxdy:
            if 0 <= x + dx < h and 0 <= y + dy < w:
                if a[x + dx][y + dy] != "#" and costs[x + dx][y + dy] == inf:
                    costs[x + dx][y + dy] = costs[x][y] + 1
                    todo.append((x + dx, y + dy))
    return costs


sx, sy = -1, -1
gx, gy = -1, -1
points = []
for x in range(h):
    for y in range(w):
        if a[x][y] == "S":
            sx = x
            sy = y
        elif a[x][y] == "G":
            gx = x
            gy = y
        elif a[x][y] == "o":
            points.append((x, y))

points = [(gx, gy)] + points + [(sx, sy)]
n = len(points)

costs = [[0] * n for _ in range(n)]
for i in range(n):
    xi, yi = points[i]
    distances = bfs(xi, yi)
    for j in range(n):
        xj, yj = points[j]
        costs[i][j] = distances[xj][yj]

n -= 1
dp = [[inf] * (1 << n) for _ in range(n)]
for i in range(1, n):
    dp[i][1 << i] = costs[n][i]

for mask in range(1, 1 << n):
    for i in range(1, n):
        if dp[i][mask] > t:
            continue
        for j in range(n):
            if (mask >> j) & 1:
                continue
            dp[j][mask | (1 << j)] = min(dp[j][mask | (1 << j)], dp[i][mask] + costs[i][j])


def popcount(x):
    return bin(x).count("1")


ans = -1
if costs[0][n] <= t:
    ans = 0
for mask in range(1 << n):
    if dp[0][mask] <= t:
        ans = max(ans, popcount(mask) - 1)
print(ans)
