def main():
    N = int(input())
    G = [list(input()) for _ in range(N)]
    for i in range(N):
        for j in range(N - 5):
            if sum(G[i][j + k] == "#" for k in range(6)) >= 4:
                print("Yes")
                exit()

    for i in range(N - 5):
        for j in range(N):
            if sum(G[i + k][j] == "#" for k in range(6)) >= 4:
                print("Yes")
                exit()

    for i in range(N - 5):
        for j in range(N - 5):
            if (
                sum(G[i + k][j + k] == "#" for k in range(6)) >= 4
                or sum(G[i + 5 - k][j + k] == "#" for k in range(6)) >= 4
            ):
                print("Yes")
                exit()
    print("No")


if __name__ == "__main__":
    main()
