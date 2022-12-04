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

    s = input()
    print(2 * s.count("w") + s.count("v"))


if __name__ == '__main__':
    main()
