from functools import reduce


def main():
    N = int(input())
    A = list(map(int, input().split()))
    s = reduce(lambda x, y: x * y, A)
    print(s / sum(map(lambda x: s // x, A)))


if __name__ == "__main__":
    main()
