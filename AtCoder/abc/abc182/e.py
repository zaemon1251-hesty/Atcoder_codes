def main():
    H, W, N, M = map(int, input().split())
    light = [list(map(lambda x: int(x) - 1, input().split())) for _ in range(N)]
    block = [list(map(lambda x: int(x) - 1, input().split())) for _ in range(M)]
    hlighten = [[0] * W for _ in range(H)]
    wlighten = [[0] * W for _ in range(H)]
    for c, d in block:
        hlighten[c][d] = wlighten[c][d] = 2
    for a, b in light:
        # 縦方向の光の処理。既に光がある場合は無視し、ないなら縦方向に光を照らす。
        if hlighten[a][b] == 0:
            hlighten[a][b] = 1
            for f in [1, -1]:
                t = a
                t += f
                while 0 <= t < H and hlighten[t][b] != 2:
                    hlighten[t][b] = 1
                    t += f
        # 横方向の光の処理。
        if wlighten[a][b] == 0:
            wlighten[a][b] = 1
            for f in [1, -1]:
                s = b
                s += f
                while 0 <= s < W and wlighten[a][s] != 2:
                    wlighten[a][s] = 1
                    s += f

    ans = 0
    for i in range(H):
        for j in range(W):
            ans += hlighten[i][j] == 1 or wlighten[i][j] == 1
    print(ans)


if __name__ == "__main__":
    main()
