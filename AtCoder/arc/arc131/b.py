H, W = map(int, input().split())
C = [list(input()) for _ in range(H)]
s = {"1", "2", "3", "4", "5"}
dxy = [(-1, 0), (1, 0), (0, -1), (0, 1)]
for i in range(H):
    for j in range(W):
        if C[i][j] == ".":
            used = set()
            for dx, dy in dxy:
                nx = i + dx
                ny = j + dy
                if 0 <= nx < H and 0 <= ny < W and C[nx][ny] in s:
                    used.add(C[nx][ny])
            C[i][j] = list(s - used)[0]
print(*["".join(c) for c in C], sep="\n")
