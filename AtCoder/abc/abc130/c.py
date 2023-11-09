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

    H, W, x, y = mi()
    ans_dup = "1" if x == H / 2 and y == W / 2 else "0"
    print(H * W / 2, ans_dup)


if __name__ == "__main__":
    main()
