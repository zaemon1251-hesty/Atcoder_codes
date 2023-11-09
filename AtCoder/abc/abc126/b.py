import sys


def input():
    return sys.stdin.readline().rstrip()


def is_month(s: str):
    if 0 < int(s) <= 12:
        return True

    return False


def main():
    def li():
        return list(map(int, input().split()))

    def mi():
        return map(int, input().split())

    def ii():
        return int(input())

    S = input()
    src, dst = S[:2], S[2:]

    if is_month(src) and is_month(dst):
        print("AMBIGUOUS")
    elif is_month(src) and not is_month(dst):
        print("MMYY")
    elif not is_month(src) and is_month(dst):
        print("YYMM")
    else:
        print("NA")


if __name__ == "__main__":
    main()
