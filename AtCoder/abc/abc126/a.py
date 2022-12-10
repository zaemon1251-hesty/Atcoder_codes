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
    N, K = mi()
    S = list(input())
    S[K - 1] = S[K - 1].lower()
    print("".join(S))


if __name__ == '__main__':
    main()
