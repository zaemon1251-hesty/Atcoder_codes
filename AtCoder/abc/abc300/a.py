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

    N, A, B = mi()
    C = li()
    print(C.index(A + B) + 1)


if __name__ == "__main__":
    main()
