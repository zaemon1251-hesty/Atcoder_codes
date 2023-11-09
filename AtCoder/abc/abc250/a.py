def main():
    H, W = map(int, input().split())
    R, C = map(int, input().split())
    ans = 0
    for nx in range(1, H + 1):
        for ny in range(1, W + 1):
            ans += abs(R - nx) + abs(C - ny) == 1
    print(ans)


if __name__ == "__main__":
    main()
