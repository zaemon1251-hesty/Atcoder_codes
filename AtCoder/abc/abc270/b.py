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

    X, Y, Z = mi()
    if X < 0:
        X *= -1
        Y *= -1
        Z *= -1

    if 0 < Y < X:
        if Z < 0:
            print(X - 2 * Z)
        elif 0 < Z < Y:
            print(X)
        else:
            print(-1)

    else:
        print(X)


if __name__ == "__main__":
    main()
