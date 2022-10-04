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
    num = "-1"
    ans = -1
    modd = [0] * 10
    for i in range(1, N + 1):
        for d in range(1, 10):
            modd[d] = (modd[d] * 10 + d) % M
            if modd[d] == 0:
                num = "%s" % d
                ans = i
    print(-1 if ans == -1 else num * ans)


if __name__ == '__main__':
    main()
