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

    t = input()
    s = input()
    ns = len(s)
    nt = len(t)
    for i in range(nt - ns + 1):
        for j in range(i + ns, nt + 2):
            if s == t[i:j]:
                print("Yes")
                return

    print("No")


if __name__ == "__main__":
    main()
