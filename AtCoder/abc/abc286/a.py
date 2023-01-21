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
    N, P, Q, R, S = mi()
    A = li()
    A[P - 1:Q], A[R - 1:S] = A[R - 1:S], A[P - 1:Q]
    print(*A)


if __name__ == '__main__':
    main()
