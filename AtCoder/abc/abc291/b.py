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

    N = ii()
    X = sorted(li())
    print(sum(X[N:-N]) / 3 / N)


if __name__ == '__main__':
    main()
