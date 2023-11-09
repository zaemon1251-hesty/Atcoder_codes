def main():
    H, W = map(int, input().split())
    G = [list(input()) for _ in range(H)]
    movemap = {"U": (-1, 0), "D": (1, 0), "L": (0, -1), "R": (0, 1)}
    seen = [[False] * W for _ in range(H)]
    x, y = 0, 0
    while True:
        seen[x][y] = True

        dx, dy = movemap[G[x][y]]
        nx, ny = x + dx, y + dy

        if nx < 0 or nx >= H or ny < 0 or ny >= W:
            break
        if seen[nx][ny]:
            print(-1)
            exit()

        x, y = nx, ny
    print(x + 1, y + 1)


if __name__ == "__main__":
    main()
