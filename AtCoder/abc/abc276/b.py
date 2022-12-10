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

    N, M = mi()
    towns = [[] for _ in range(N)]
    for _ in range(M):
        a, b = mi()
        towns[a - 1].append(b)
        towns[b - 1].append(a)

    for i in range(N):
        print(len(towns[i]), *sorted(towns[i]))


if __name__ == '__main__':
    main()
