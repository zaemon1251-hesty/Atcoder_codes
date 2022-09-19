import sys
# def input(): return sys.stdin.readline().rstrip()


def ask(a, b, c, d):
    print(f"? {a} {b} {c} {d}")
    res = int(input())
    if res == -1:
        exit()

    return res


def main():
    def li(): return list(map(int, input().split()))
    def mi(): return map(int, input().split())
    def ii(): return int(input())

    N = ii()
    a, b = 1, N + 1
    while b - a > 1:
        c = (b + a) // 2
        res = ask(a, c - 1, 1, N)
        if res == c - a:
            a = c
        else:
            b = c

    c, d = 1, N + 1
    while d - c > 1:
        e = (c + d) // 2
        res = ask(1, N, c, e - 1)
        if res == e - c:
            c = e
        else:
            d = e

    print(f"! {a} {c}")


if __name__ == '__main__':
    main()
