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
    S = input()
    A = S.count("A")
    if A > N - A:
        print("A")
    elif A < N - A:
        print("T")
    else:
        if S[-1] == "T":
            print("A")
        else:
            print("T")


if __name__ == "__main__":
    main()
