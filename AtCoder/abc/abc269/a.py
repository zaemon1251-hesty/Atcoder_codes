import sys
def input(): return sys.stdin.readline().rstrip()


def main():
    def li(): return list(map(int, input().split()))
    def mi(): return map(int, input().split())
    def ii(): return int(input())

    a, b, c, d = mi()
    print((a + b) * (c - d))
    print("Takahashi")


if __name__ == '__main__':
    main()
