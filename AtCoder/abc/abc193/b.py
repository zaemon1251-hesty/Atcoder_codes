def main():
    N = int(input())
    S = [list(map(int, input().split())) for _ in range(N)]
    inf = 1 << 60
    ans = inf
    for a, p, x in S:
        if x > a:
            ans = min(ans, p)
    print(ans if ans < inf else -1)


if __name__ == '__main__':
    main()
