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
    N, Q = mi()

    que = [li() for _ in range(Q)]
    following = set()

    for t, a, b in que:
        if t == 1:
            following.add((a, b))
        elif t == 2:
            following.discard((a, b))
        else:
            if (a, b) in following and (b, a) in following:
                print("Yes")
            else:
                print("No")


if __name__ == '__main__':
    main()
