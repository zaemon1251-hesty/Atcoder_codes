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

    A, B = mi()
    print((A + B - 1) // B)


if __name__ == "__main__":
    main()
