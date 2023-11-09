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

    MOD = 998244353
    A, B, C, D, E, F = mi()
    print((A * B * C - D * E * F) % MOD)


if __name__ == "__main__":
    main()
