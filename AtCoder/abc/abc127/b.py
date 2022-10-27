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

    r, D, x = mi()
    for i in range(10):
        x = r * x - D
        print(x)


if __name__ == '__main__':
    main()
