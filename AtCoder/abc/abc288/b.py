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
    S = [input() for _ in range(N)]
    print(*sorted(S[:K]), sep="\n")


if __name__ == '__main__':
    main()
