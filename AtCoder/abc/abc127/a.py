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

    if A < 6:
        print(0)
    elif 6 <= A < 13:
        print(B // 2)
    else:
        print(B)


if __name__ == "__main__":
    main()
