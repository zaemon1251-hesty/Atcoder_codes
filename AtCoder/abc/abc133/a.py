def main():
    N, A, B = map(int, input().split())
    if N * A > B:
        print(B)
    else:
        print(N * A)


if __name__ == '__main__':
    main()
