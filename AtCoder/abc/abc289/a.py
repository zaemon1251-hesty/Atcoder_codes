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

    s = input()
    print(s.replace("1", "x").replace("0", "1").replace("x", "0"))


if __name__ == "__main__":
    main()
