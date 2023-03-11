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

    N, M = mi()
    A = li()
    B = li()
    print(sum(A[B[i] - 1] for i in range(M)))


if __name__ == '__main__':
    main()
