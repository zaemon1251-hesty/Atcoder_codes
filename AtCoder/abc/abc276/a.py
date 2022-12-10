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

    S = input()

    try:
        print(len(S) - S[::-1].index("a"))
    except ValueError:
        print(-1)


if __name__ == '__main__':
    main()
