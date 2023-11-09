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
    S = li()
    A = [S[0]]
    for i in range(N - 1):
        A.append(S[i + 1] - S[i])
    print(*A)


if __name__ == "__main__":
    main()
