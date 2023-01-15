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
    a, b = mi()
    a, b = min(a, b), max(a, b)
    if b // 2 == a:
        print("Yes")
    else:
        print("No")


if __name__ == '__main__':
    main()
