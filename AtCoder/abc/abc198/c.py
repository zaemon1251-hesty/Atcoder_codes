from math import sqrt, ceil


def main():
    R, X, Y = map(int, input().split())
    ok = 0
    ng = 10**9 + 1
    dist = X**2 + Y**2
    if X == 0 and Y == 0:
        print(0)
        exit()
    if R**2 > dist:
        print(2)
        exit()
    while ng - ok > 1:
        cen = (ok + ng) // 2
        if R**2 * cen**2 < dist:
            ok = cen
        else:
            ng = cen
    print(ok + 1)


if __name__ == '__main__':
    main()
