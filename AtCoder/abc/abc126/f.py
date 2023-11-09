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

    M, K = mi()
    if K >= 1 << M:
        print(-1)
        exit()
    if M == 0:
        print(0, 0)
    elif M == 1:
        if K == 0:
            ans = [0, 0, 1, 1]
            print(*ans)
        else:
            print(-1)
    else:
        b = [i for i in range(1 << M) if i != K]
        ans = b + [K] + b[::-1] + [K]
        print(*ans)


if __name__ == "__main__":
    main()
