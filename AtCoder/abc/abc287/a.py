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
    S = [input() for i in range(N)]
    if S.count("For") > N // 2:
        print("Yes")
    else:
        print("No")


if __name__ == "__main__":
    main()
