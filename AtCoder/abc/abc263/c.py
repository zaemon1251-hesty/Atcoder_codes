from itertools import combinations


def main():
    N, M = map(int, input().split())
    for s in combinations(range(1, M + 1), N):
        print(*s, end=" \n")


if __name__ == '__main__':
    main()
