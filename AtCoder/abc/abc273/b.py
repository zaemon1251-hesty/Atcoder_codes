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

    X, K = mi()
    for i in range(1, K + 1):
        g = X // 10 ** (i)
        r = X % 10**i
        if len(str(r)) == i and str(r)[0] >= "5":
            g += 1
        X = g * 10**i
    print(X)


if __name__ == "__main__":
    main()
