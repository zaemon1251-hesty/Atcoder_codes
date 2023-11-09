from functools import cmp_to_key


def func(si, sj):
    return sj[0] * si[1] > si[0] * sj[1]


def cnt(s):
    x, y, po = 0, 0, 0
    for si in s:
        if si == "X":
            x += 1
        else:
            y += int(si)
            po += x * int(si)
    return (x, y, po)


def main():
    N = int(input())
    S = [input() for _ in range(N)]
    S = map(cnt, S)

    S = sorted(S, key=lambda x: x[1] / x[0] if x[0] > 0 else float("inf"))

    ans = 0
    curx = 0
    for x, y, po in S:
        ans += curx * y + po
        curx += x
    print(ans)


if __name__ == "__main__":
    main()
