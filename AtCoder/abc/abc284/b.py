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

    T = ii()

    for _ in range(T):
        _ = ii()
        A = li()
        print(sum(a % 2 == 1 for a in A))


if __name__ == "__main__":
    main()
