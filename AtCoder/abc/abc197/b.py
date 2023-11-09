def main():
    H, W, X, Y = map(int, input().split())
    G = [list(input()) for _ in range(H)]
    X, Y = X - 1, Y - 1
    ans = 1

    cnt = 1
    while X + cnt < H and G[X + cnt][Y] == ".":
        ans += 1
        cnt += 1

    cnt = 1
    while X - cnt >= 0 and G[X - cnt][Y] == ".":
        ans += 1
        cnt += 1

    cnt = 1
    while Y + cnt < W and G[X][Y + cnt] == ".":
        ans += 1
        cnt += 1

    cnt = 1
    while Y - cnt >= 0 and G[X][Y - cnt] == ".":
        ans += 1
        cnt += 1

    print(ans)


if __name__ == "__main__":
    main()
