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

    N = ii()
    S = list(input())
    trail = set([(0, 0)])
    x, y = 0, 0

    for s in S:
        if s == "R":
            x += 1
        elif s == "L":
            x -= 1
        elif s == "U":
            y += 1
        else:
            y -= 1

        if (x, y) in trail:
            print("Yes")
            return
        trail.add((x, y))

    print("No")


if __name__ == '__main__':
    main()
