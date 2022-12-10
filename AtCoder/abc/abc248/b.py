def main():
    A, B, K = map(int, input().split())
    i = 0
    while A < B:
        A *= K
        i += 1
    print(i)


if __name__ == '__main__':
    main()
