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

    _ = ii()
    S = input()
    S = S.replace("na", "nya", -1)
    print(S)


if __name__ == '__main__':
    main()
