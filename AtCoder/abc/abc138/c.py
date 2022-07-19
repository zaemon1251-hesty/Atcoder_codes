from functools import reduce


def main():
    N = int(input())
    A = sorted(map(int, input().split()))
    print(reduce(lambda x, y: (x + y) / 2, A))


if __name__ == '__main__':
    main()
