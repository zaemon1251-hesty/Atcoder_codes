# 01 bfs

from collections import deque


H, W = map(int, input().split())
C = tuple(map(lambda x: int(x) - 1, input().split()))
D = tuple(map(lambda x: int(x) - 1, input().split()))
G = [list(input()) for _ in range(H)]


def movable(x, y):
    if x < 0 or x >= H or y < 0 or y >= W:
        return False
    if G[x][y] == "#":
        return False
    return True


inf = 1 << 60
dp = [[inf] * W for _ in range(H)]
todo = deque([C])
dp[C[0]][C[1]] = 0
mx = [0, 1, 0, -1]
my = [1, 0, -1, 0]
while todo:
    x, y = todo.popleft()
    for dx, dy in zip(mx, my):
        nx, ny = x + dx, y + dy
        if movable(nx, ny) and dp[nx][ny] > dp[x][y]:
            dp[nx][ny] = dp[x][y]
            todo.appendleft((nx, ny))
    for dx in range(-2, 3):
        for dy in range(-2, 3):
            nx, ny = x + dx, y + dy
            if movable(nx, ny) and dp[nx][ny] > dp[x][y] + 1:
                dp[nx][ny] = dp[x][y] + 1
                todo.append((nx, ny))
print(dp[D[0]][D[1]] if dp[D[0]][D[1]] < inf else -1)
