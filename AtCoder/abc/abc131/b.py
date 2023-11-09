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

    N, L = mi()
    ans = 1 << 60
    res = -1
    total = N * L + N * (N - 1) // 2
    for i in range(N):
        apple = L + i
        cand = abs(apple)
        if cand < ans:
            ans = cand
            res = total - apple
    print(res)


if __name__ == "__main__":
    main()
