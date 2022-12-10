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

    H, W = mi()
    C = [input() for _ in range(H)]
    ans = []
    for w in range(W):
        ans.append(sum(C[i][w] == "#" for i in range(H)))
    print(*ans)


if __name__ == '__main__':
    main()
