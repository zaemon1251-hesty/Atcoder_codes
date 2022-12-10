def main():
    N, A, B = map(int, input().split())
    G = [[-1] for _ in range(N)]
    s = [[""] * (N * B) for _ in range(N * A)]
    t = [".", "#"]
    for i in range(N):
        for j in range(N):
            w = t[(i + j) % 2]
            for a in range(i * A, (i + 1) * A):
                for b in range(j * B, (j + 1) * B):
                    s[a][b] = w
    for ss in s:
        print(*ss, sep="")


if __name__ == '__main__':
    main()
