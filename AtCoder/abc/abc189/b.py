def main():
    N, X = map(int, input().split())
    X *= 100
    A = [list(map(int, input().split())) for _ in range(N)]
    i = 1
    for v, p in A:
        if v * p > X:
            print(i)
            exit()
        X -= v * p
        i += 1
    print(-1)


if __name__ == "__main__":
    main()
