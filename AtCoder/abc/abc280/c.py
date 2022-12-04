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

    S = input()
    T = input()
    NS = len(S)

    cur = 0
    while cur < NS and S[cur] == T[cur]:
        cur += 1

    print(cur + 1)


if __name__ == '__main__':
    main()
