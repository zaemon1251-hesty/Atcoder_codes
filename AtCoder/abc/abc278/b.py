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

    H, M = mi()
    now = 60 * H + M
    while True:
        h, w = divmod(now, 60)
        h_1, h_2 = divmod(h, 10)
        w_1, w_2 = divmod(w, 10)
        newH, newM = h_1 * 10 + w_1, h_2 * 10 + w_2
        if 0 <= newH < 24 and 0 <= newM < 60:
            print(f"{h:02d} {w:02d}")
            exit()
        now += 1
        now %= 24 * 60


if __name__ == "__main__":
    main()
