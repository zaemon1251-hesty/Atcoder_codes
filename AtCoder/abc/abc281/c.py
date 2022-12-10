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

    N, T = mi()
    A = li()
    i = 0
    T %= sum(A)
    while T > 0:
        newT = max(0, T - A[i])
        if newT == 0:
            print(i + 1, T)
        i += 1
        i %= N
        T = newT


if __name__ == '__main__':
    main()
