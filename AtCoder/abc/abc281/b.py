import sys
from string import ascii_uppercase, ascii_lowercase


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

    if len(s) != 8:
        print("No")
        return

    b, s, a = s[0], s[1:-1], s[-1]

    try:
        s = int(s)
    except BaseException:
        print("No")
        return

    if not (10**5 <= s < 10**6):
        print("No")
        return

    if a not in ascii_uppercase:
        print("No")
        return

    if b not in ascii_uppercase:
        print("No")
        return

    print("Yes")


if __name__ == "__main__":
    main()
