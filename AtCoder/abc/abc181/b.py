def main():
    N = int(input())
    ans = 0
    for i in range(N):
        H, W = map(int, input().split())
        ans += (W + H) * (W - H + 1) // 2
    print(ans)


if __name__ == "__main__":
    main()
