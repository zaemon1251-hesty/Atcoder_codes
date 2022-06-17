from itertools import combinations
from math import sqrt, inf


def l2(x, y):
    return (y[0] - x[0])**2 + (y[1] - x[1])**2


def circumcircle(P1, P2, P3):
    # 外心円の中心
    x1, y1 = P1
    x2, y2 = P2
    x3, y3 = P3
    a = 2 * (x1 - x2)
    b = 2 * (y1 - y2)
    p = x1**2 - x2**2 + y1**2 - y2**2
    c = 2 * (x1 - x3)
    d = 2 * (y1 - y3)
    q = x1**2 - x3**2 + y1**2 - y3**2
    det = a * d - b * c

    if det == 0:
        return False, False, False

    x = d * p - b * q
    y = a * q - c * p
    if det < 0:
        x = -x
        y = -y
        det = -det
    x /= det
    y /= det
    r2 = (x - x1)**2 + (y - y1)**2
    return x, y, r2


def main():
    N = int(input())
    S = [list(map(int, input().split())) for _ in range(N)]
    ans = inf

    for i, j in combinations(range(N), 2):
        cen = [
            (S[i][0] + S[j][0]) / 2,
            (S[i][1] + S[j][1]) / 2
        ]

        res = l2(S[i], cen)
        for k in range(N):
            res = max(res, l2(S[k], cen))
        ans = min(ans, res)

    for i, j, k in combinations(range(N), 3):
        x, y, r = circumcircle(S[i], S[j], S[k])

        if x == False:
            continue

        cen = [
            x,
            y
        ]
        res = r
        for m in range(N):
            res = max(res, l2(S[m], cen))
        ans = min(ans, res)

    print(sqrt(ans))


if __name__ == '__main__':
    main()
