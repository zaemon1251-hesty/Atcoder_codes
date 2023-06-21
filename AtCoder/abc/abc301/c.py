import sys
from collections import Counter
from string import ascii_lowercase


def input():
    return sys.stdin.readline().rstrip()


def main():
    def li():
        return list(map(int, input().split()))

    def mi():
        return map(int, input().split())

    def ii():
        return int(input())

    S = Counter(input())
    T = Counter(input())

    for k in ascii_lowercase:
        if S[k] < T[k]:
            if k not in "atcoder":
                print("No")
                return
            if S[k] + S["@"] < T[k]:
                print("No")
                return
            S["@"] = max(0, S["@"] - (T[k] - S[k]))
        elif S[k] > T[k]:
            if k not in "atcoder":
                print("No")
                return
            if S[k] > T["@"] + T[k]:
                print("No")
                return
            T["@"] = max(0, T["@"] - (S[k] - T[k]))
        else:
            pass

    print("Yes")


if __name__ == "__main__":
    main()
