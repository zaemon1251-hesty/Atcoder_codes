def main():
    N = int(input())
    H = list(map(int, input().split()))
    if N == 1:
        print(0)
        exit()
    ans = 0
    now = 0
    for i in range(N - 2, -1, -1):
        if H[i] >= H[i + 1]:
            now += 1
            ans = max(ans, now)
        else:
            now = 0
    print(ans)


if __name__ == '__main__':
    main()
