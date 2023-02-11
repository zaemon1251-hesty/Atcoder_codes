import sys


def input():
    return sys.stdin.readline().rstrip()


def main():
    def li():
        return list(map(int, input().split()))

    def mi():
        return map(int, input().split())

    def ii():
        return int(input())

    sx, sy = mi()
    tx, ty = mi()
    a, b, c, d = mi()

    if max(a - 1 - sx, a - 1 - tx) <= min(b - 1 - sx, b - 1 - tx) and \
            max(c - 1 - sy, a - 1 - ty) <= min(d - 1 - sy, d - 1 - ty):
        print("Yes")
        mx = (max(a - 1 - sx, a - 1 - tx) + min(b - 1 - sx, b - 1 - tx)) / 2
        my = (max(c - 1 - sy, a - 1 - ty) + min(d - 1 - sy, d - 1 - ty)) / 2
        print((sx + mx) / 2, (sy + my) / 2)
        print((tx + mx) / 2, (ty + my) / 2)
    else:
        print("No")


if __name__ == '__main__':
    main()
