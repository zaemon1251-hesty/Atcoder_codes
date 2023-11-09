def main():
    def li():
        return list(map(int, input().split()))

    def mi():
        return map(int, input().split())

    def ii():
        return int(input())

    N = ii()
    D = sorted(li())
    print(D[N // 2] - D[N // 2 - 1])


if __name__ == "__main__":
    main()
