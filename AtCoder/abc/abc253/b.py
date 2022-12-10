def main():
    H, W = map(int, input().split())
    G = [list(input()) for _ in range(H)]
    set = []
    for i in range(H):
        for j in range(W):
            if G[i][j] == "o":
                set.append((i, j))
    print(abs(set[0][0] - set[1][0]) + abs(set[0][1] - set[1][1]))


if __name__ == '__main__':
    main()
