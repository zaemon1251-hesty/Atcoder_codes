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

    S = list(input())
    N = int(input())
    for i in range(len(S)):
        if S[i] != "?":
            continue

        S[i] = "1"
        if int("0b" + "".join([s if s != "?" else "0" for s in S]), 2) <= N:
            continue
        S[i] = "0"

    ans = int("0b" + "".join(S), 2)
    print(ans if ans <= N else -1)


if __name__ == "__main__":
    main()
