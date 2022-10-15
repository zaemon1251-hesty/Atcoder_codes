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

    def f(i):
        if i == 0:
            return 1
        return i * f(i - 1)
    print(f(ii()))


if __name__ == '__main__':
    main()
