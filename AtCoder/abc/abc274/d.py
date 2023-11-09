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

    N, x, y = mi()
    A = li()

    xws = set([A[0]])
    yws = set([0])

    for i in range(2, N, 2):
        tmp = set()
        for x_ in xws:
            tmp.add(x_ + A[i])
            tmp.add(x_ - A[i])
        xws = tmp

    for i in range(1, N, 2):
        tmp = set()
        for y_ in yws:
            tmp.add(y_ + A[i])
            tmp.add(y_ - A[i])
        yws = tmp

    print("Yes" if (x in xws and y in yws) else "No")


if __name__ == "__main__":
    main()
