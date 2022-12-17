import sys

from string import ascii_uppercase


def input():
    return sys.stdin.readline().rstrip()


def main():
    def li():
        return list(map(int, input().split()))

    def mi():
        return map(int, input().split())

    def ii():
        return int(input())
    K = ii()
    print(ascii_uppercase[:K])


if __name__ == '__main__':
    main()
