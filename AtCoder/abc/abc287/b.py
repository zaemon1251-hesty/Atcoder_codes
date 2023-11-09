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
    S = [input() for i in range(N)]
    T = [input() for i in range(M)]
    sufs = set(T)
    print(sum((s[3:] in sufs) for s in S))


if __name__ == "__main__":
    main()
