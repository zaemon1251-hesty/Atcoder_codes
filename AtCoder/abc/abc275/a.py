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

    _ = ii()
    H = li()
    print(H.index(max(H)) + 1)


if __name__ == "__main__":
    main()
