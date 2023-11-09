def sqrt_floor(a: int):
    ok = 0
    ng = 10**9 + 1
    while ng - ok >= 2:
        mid = ok + (ng - ok) // 2
        if mid**2 <= a:
            ok = mid
        else:
            ng = mid
    return ok


def toint(i: str):
    c = i.split(".")
    c.append("0" * (4 - len(c[1]) if len(c) == 2 else 4))
    return int("".join(c))


def divceil(x, m):
    return (x + m - 1) // m


def main():
    X, Y, R = map(lambda x: toint(str(x)), input().split())
    st = divceil(X - R, 10000) * 10000
    st_r = st - X
    ans = 0
    for p in range(st_r, R + 1, 10000):
        r = sqrt_floor(R**2 - p**2)
        l = divceil(Y - r, 10000)
        h = (Y + r) // 10000
        ans += h - l + 1
    print(ans)


if __name__ == "__main__":
    main()
