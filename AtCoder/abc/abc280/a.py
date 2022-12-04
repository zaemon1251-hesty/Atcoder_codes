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
    H, W = mi()
    S = [input() for _ in range(H)]
    print(sum(s.count("#") for s in S))


if __name__ == '__main__':
    main()
