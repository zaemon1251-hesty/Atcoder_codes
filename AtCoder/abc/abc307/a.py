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
    A = li()
    buf = []
    for i in range(N):
        ans = 0
        for j in range(7):
            ans += A[7 * i + j]
        buf.append(ans)
    print(*buf)


if __name__ == "__main__":
    main()
