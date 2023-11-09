def main():
    N = int(input())
    S = [list(map(int, input().split())) for _ in range(N)]
    aoki = sum(s[0] for s in S)
    taka = 0
    S.sort(key=lambda x: (2 * x[0] + x[1]))
    ans = 0
    while aoki >= taka:
        a, b = S.pop()
        taka += 2 * a + b
        ans += 1
    print(ans)


if __name__ == "__main__":
    main()
