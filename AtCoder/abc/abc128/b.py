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
    restaurants = []
    for i in range(N):
        s, p = map(str, input().split())
        restaurants.append((s, p, i + 1))
    restaurants.sort(key=lambda x: (x[0], -int(x[1])))
    print(*[i for (_, _, i) in restaurants], sep="\n")


if __name__ == '__main__':
    main()
