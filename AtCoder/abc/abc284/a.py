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

    n = ii()
    s = [input() for _ in range(n)]
    print(*s[::-1], sep="\n")


if __name__ == "__main__":
    main()
