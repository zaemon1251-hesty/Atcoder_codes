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

    N, M, D = mi()
    A = sorted(li())
    B = sorted(li())

    ans = -1
    while A and B:
        if abs(A[-1] - B[-1]) <= D:
            ans = max(ans, A[-1] + B[-1])
            A.pop()
            B.pop()
        elif A[-1] > B[-1]:
            A.pop()
        else:
            B.pop()
    print(ans)


if __name__ == "__main__":
    main()
