def main():
    N, a, b = map(int, input().split())
    A = sorted(map(int, input().split()))

    def check(x):
        debut = 0
        for i in range(N):
            if x > A[i]:
                debut += (x - A[i] + a - 1) // a
            else:
                payback = (A[i] - x) // b
                debut = max(debut - payback, 0)
        return debut == 0

    ok = 1
    ng = 10**9 + 1
    while ng - ok > 1:
        cen = (ng + ok) // 2
        if check(cen):
            ok = cen
        else:
            ng = cen
    print(ok)


if __name__ == '__main__':
    main()
