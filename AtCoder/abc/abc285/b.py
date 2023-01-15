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
    S = "Z" + input()
    for i in range(1, N):
        k = 1
        while k + i <= N and S[k] != S[i + k]:
            k += 1
        print(k - 1)


if __name__ == '__main__':
    main()
